from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class DesarrolladorHabilidad(Base):
    __tablename__ = 'desarrollador_habilidad'
    
    id = Column(BigInteger, primary_key=True)
    desarrollador_id = Column(BigInteger, ForeignKey('desarrolladores.id'), nullable=False)
    habilidad_id = Column(BigInteger, ForeignKey('habilidades.id'), nullable=False)
    nivel = Column(Integer, nullable=False)
    
    # Relationships
    desarrollador = relationship("Desarrollador", back_populates="desarrollador_habilidades")
    habilidad = relationship("Habilidad", back_populates="desarrollador_habilidades")
