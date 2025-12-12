from sqlalchemy import String, Text, BigInteger, Integer, Date, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class Way(Base):
    __tablename__ = "way"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    address: Mapped[str] = mapped_column(Text, nullable=False)

    user = relationship("User", back_populates="way", uselist=False)

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)  # hash
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    way_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("way.id", onupdate="CASCADE", ondelete="SET NULL"),
        unique=True,
        nullable=True
    )

    way = relationship("Way", back_populates="user")

class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    active_principle: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    producer: Mapped[str | None] = mapped_column(String(255), nullable=True)
    preservation: Mapped[str | None] = mapped_column(Text, nullable=True)
    contraindication: Mapped[str | None] = mapped_column(Text, nullable=True)
    side_effect: Mapped[str | None] = mapped_column(Text, nullable=True)  # "vomito,nausea"

class Inventary(Base):
    __tablename__ = "inventary"
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="ck_inventary_quantity_nonneg"),
    )

    id_medicine: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("medicine.id", onupdate="CASCADE", ondelete="RESTRICT"),
        primary_key=True
    )
    expire_date: Mapped[str] = mapped_column(Date, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
