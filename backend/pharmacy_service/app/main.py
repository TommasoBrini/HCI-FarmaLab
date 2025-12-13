from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from . import models, schemas, crud
from datetime import date 

app = FastAPI(title="Pharmacy Inventory Service", version="1.0.0")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ways", response_model=schemas.WayOut, status_code=201)
def create_way(payload: schemas.WayCreate, db: Session = Depends(get_db)):
    return crud.create_way(db, payload)

@app.post("/users", response_model=schemas.UserOut, status_code=201)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user = crud.create_user(db, payload)
        return user
    except Exception as e:
        # es: email duplicata / vincolo unique(way_id)
        raise HTTPException(status_code=400, detail="Cannot create user (duplicate email or way_id).") from e

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/medicines", response_model=schemas.MedicineOut, status_code=201)
def create_medicine(payload: schemas.MedicineCreate, db: Session = Depends(get_db)):
    med = crud.create_medicine(db, payload)
    return schemas.MedicineOut.model_validate(med, from_attributes=True)


@app.get("/medicines/{medicine_id}", response_model=schemas.MedicineOut)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    med = crud.get_medicine(db, medicine_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return schemas.MedicineOut.model_validate(med, from_attributes=True)

@app.put("/inventary", response_model=schemas.InventaryOut)
def upsert_inventary(payload: schemas.InventaryUpsert, db: Session = Depends(get_db)):
    # verifica esistenza medicine
    if not crud.get_medicine(db, payload.id_medicine):
        raise HTTPException(status_code=400, detail="Medicine does not exist")
    return crud.upsert_inventary(db, payload)

@app.get("/inventary", response_model=list[schemas.InventaryOutDetailed])
def get_inventary(db: Session = Depends(get_db)):
    rows = crud.list_inventary_detailed(db)
    return [
        schemas.InventaryOutDetailed(
            id_medicine=r[0],
            medicine_name=r[1],
            active_principle=r[2],
            expire_date=r[3],
            quantity=r[4],
        )
        for r in rows
    ]

@app.patch("/inventary/{id_medicine}/{expire_date}", response_model=schemas.InventaryOut)
def patch_inventary_quantity(
    id_medicine: int,
    expire_date: date,
    payload: schemas.InventaryUpdateQuantity,
    db: Session = Depends(get_db),
):
    updated = crud.update_inventary_quantity(db, id_medicine, expire_date, payload.quantity)
    if not updated:
        raise HTTPException(status_code=404, detail="Inventary row not found")
    return updated

@app.delete("/inventary/{id_medicine}/{expire_date}", status_code=204)
def delete_inventary(
    id_medicine: int,
    expire_date: date,
    db: Session = Depends(get_db),
):
    ok = crud.delete_inventary_row(db, id_medicine, expire_date)
    if not ok:
        raise HTTPException(status_code=404, detail="Inventary row not found")
    return
