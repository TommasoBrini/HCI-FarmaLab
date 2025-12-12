from datetime import date
from pydantic import BaseModel, EmailStr, Field

# WAY
class WayCreate(BaseModel):
    address: str

class WayOut(BaseModel):
    id: int
    address: str
    class Config:
        from_attributes = True

# USER
class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str = Field(min_length=8)
    role: str
    way_id: int | None = None

class UserOut(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    role: str
    way: WayOut | None = None
    class Config:
        from_attributes = True

# MEDICINE
class MedicineCreate(BaseModel):
    name: str
    active_principle: str
    producer: str | None = None
    preservation: str | None = None
    contraindication: str | None = None
    side_effect: list[str] | None = None  # in API come lista

class MedicineOut(BaseModel):
    id: int
    name: str
    active_principle: str
    producer: str | None = None
    preservation: str | None = None
    contraindication: str | None = None
    side_effect: list[str] | None = None
    class Config:
        from_attributes = True

# INVENTARY
class InventaryUpsert(BaseModel):
    id_medicine: int
    expire_date: date
    quantity: int = Field(ge=0)

class InventaryOut(BaseModel):
    id_medicine: int
    expire_date: date
    quantity: int
    class Config:
        from_attributes = True

class InventaryOutDetailed(BaseModel):
    id_medicine: int
    medicine_name: str
    active_principle: str
    expire_date: date
    quantity: int

class InventaryUpdateQuantity(BaseModel):
    quantity: int = Field(ge=0)