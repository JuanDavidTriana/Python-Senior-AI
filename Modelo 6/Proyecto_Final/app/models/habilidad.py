from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from .base import Base


class Habilidad(Base):
    __tablename__ = 'habilidades'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    categoria = Column(String(255), nullable=False)
    
    # Relationships
    desarrollador_habilidades = relationship("DesarrolladorHabilidad", back_populates="habilidad")
