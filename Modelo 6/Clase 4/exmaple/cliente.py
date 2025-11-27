from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)


