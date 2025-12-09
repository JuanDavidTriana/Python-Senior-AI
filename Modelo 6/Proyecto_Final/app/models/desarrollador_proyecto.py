from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class DesarrolladorProyecto(Base):
    __tablename__ = 'desarrollador_proyecto'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    desarrollador_id = Column(BigInteger, ForeignKey('desarrolladores.id'), nullable=False)
    proyecto_id = Column(BigInteger, ForeignKey('proyectos.id'), nullable=False)
    rol_en_proyecto = Column(String(255), nullable=False)
    
    # Relationships
    desarrollador = relationship("Desarrollador", back_populates="desarrollador_proyectos")
    proyecto = relationship("Proyecto", back_populates="desarrollador_proyectos")
