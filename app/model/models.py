from app.model.database import Base
from sqlalchemy import Column, Integer, Unicode, DateTime


class Compra(Base):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)