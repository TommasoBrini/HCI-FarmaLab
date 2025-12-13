from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas, security

def _join_list(values: list[str] | None) -> str | None:
    if not values:
        return None
    # pulizia minima
    cleaned = [v.strip() for v in values if v.strip()]
    return ",".join(cleaned) if cleaned else None

def _split_csv(value: str | None) -> list[str] | None:
    if not value:
        return None
    items = [x.strip() for x in value.split(",") if x.strip()]
    return items or None

# WAY
def create_way(db: Session, payload: schemas.WayCreate) -> models.Way:
    way = models.Way(address=payload.address)
    db.add(way)
    db.commit()
    db.refresh(way)
    return way

# USER
def create_user(db: Session, payload: schemas.UserCreate) -> models.User:
    user = models.User(
        name=payload.name,
        surname=payload.surname,
        email=str(payload.email),
        password=security.hash_password(payload.password),
        role=payload.role,
        way_id=payload.way_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> models.User | None:
    return db.get(models.User, user_id)

# MEDICINE
def create_medicine(db: Session, payload: schemas.MedicineCreate) -> models.Medicine:
    med = models.Medicine(
        name=payload.name,
        active_principle=payload.active_principle,
        producer=payload.producer,
        preservation=payload.preservation,
        contraindication=payload.contraindication,
        side_effect=_join_list(payload.side_effect),
        image=str(payload.image) if payload.image else None,
    )
    db.add(med)
    db.commit()
    db.refresh(med)
    return med

def get_medicine(db: Session, medicine_id: int) -> models.Medicine | None:
    return db.get(models.Medicine, medicine_id)

# INVENTARY (upsert su PK composta)
def upsert_inventary(db: Session, payload: schemas.InventaryUpsert) -> models.Inventary:
    row = db.get(models.Inventary, {"id_medicine": payload.id_medicine, "expire_date": payload.expire_date})
    if row:
        row.quantity = payload.quantity
    else:
        row = models.Inventary(
            id_medicine=payload.id_medicine,
            expire_date=payload.expire_date,
            quantity=payload.quantity
        )
        db.add(row)
    db.commit()
    db.refresh(row)
    return row

def list_inventary(db: Session) -> list[models.Inventary]:
    stmt = select(models.Inventary).order_by(models.Inventary.expire_date.asc())
    return list(db.execute(stmt).scalars().all())

def list_inventary_detailed(db: Session):
    # ritorna righe joinate (inventary + medicine)
    stmt = (
        select(
            models.Inventary.id_medicine,
            models.Medicine.name,
            models.Medicine.active_principle,
            models.Inventary.expire_date,
            models.Inventary.quantity,
        )
        .join(models.Medicine, models.Medicine.id == models.Inventary.id_medicine)
        .order_by(models.Medicine.name.asc(), models.Inventary.expire_date.asc())
    )
    return db.execute(stmt).all()

def update_inventary_quantity(db: Session, id_medicine: int, expire_date, quantity: int) -> models.Inventary | None:
    row = db.get(models.Inventary, {"id_medicine": id_medicine, "expire_date": expire_date})
    if not row:
        return None
    row.quantity = quantity
    db.commit()
    db.refresh(row)
    return row

def delete_inventary_row(db: Session, id_medicine: int, expire_date) -> bool:
    row = db.get(models.Inventary, {"id_medicine": id_medicine, "expire_date": expire_date})
    if not row:
        return False
    db.delete(row)
    db.commit()
    return True
