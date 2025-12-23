from sqlalchemy.orm import Session
from sqlalchemy import select, func

from .db import SessionLocal
from . import models


WAYS_SEED = [
    "Via Roma 10, Milano",
    "Via Garibaldi 25, Torino",
    "Corso Italia 3, Firenze",
    "Viale Europa 120, Bologna",
    "Piazza Duomo 1, Milano",
]

MEDICINES_SEED = [
    {
        "name": "Tachipirina",
        "active_principle": "Paracetamolo",
        "producer": "Angelini",
        "preservation": "Conservare sotto i 25°C",
        "contraindication": "Insufficienza epatica grave",
        "side_effect": "nausea,vomito,cefalea",
        "image": "https://example.com/images/tachipirina.png",
    },
    {
        "name": "Aspirina",
        "active_principle": "Acido acetilsalicilico",
        "producer": "Bayer",
        "preservation": "Conservare in luogo asciutto",
        "contraindication": "Ulcera peptica attiva",
        "side_effect": "gastrite,nausea",
        "image": "https://example.com/images/aspirina.png",
    },
    {
        "name": "Brufen",
        "active_principle": "Ibuprofene",
        "producer": "Abbott",
        "preservation": "Conservare sotto i 25°C",
        "contraindication": "Gravidanza terzo trimestre",
        "side_effect": "dolore addominale,nausea,capogiri",
        "image": "https://example.com/images/brufen.png",
    },
    {
        "name": "Zyrtec",
        "active_principle": "Cetirizina",
        "producer": "UCB",
        "preservation": "Conservare in confezione originale",
        "contraindication": "Ipersensibilità al principio attivo",
        "side_effect": "sonnolenza,bocca secca",
        "image": "https://example.com/images/zyrtec.png",
    },
]


def _table_count(db: Session, model) -> int:
    return db.execute(select(func.count()).select_from(model)).scalar_one()


def populate_db_if_empty() -> None:
    """
    Popola WAY e MEDICINE SOLO se le tabelle sono vuote.
    Idempotente: se ci sono già record, non fa nulla.
    """
    db = SessionLocal()
    try:
        way_count = _table_count(db, models.Way)
        med_count = _table_count(db, models.Medicine)

        if way_count == 0:
            db.add_all([models.Way(address=a) for a in WAYS_SEED])

        if med_count == 0:
            db.add_all([models.Medicine(**m) for m in MEDICINES_SEED])

        if way_count == 0 or med_count == 0:
            db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()