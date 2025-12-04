from sqlalchemy import Column, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class TareaAsignacion(Base):
    __tablename__ = 'tarea_asignacion'
    
    id = Column(BigInteger, primary_key=True)
    tarea_id = Column(BigInteger, ForeignKey('tareas.id'), nullable=False)
    desarrollador_id = Column(BigInteger, ForeignKey('desarrolladores.id'), nullable=False)
    fecha_asignacion = Column(DateTime, nullable=False)
    
    # Relationships
    tarea = relationship("Tarea", back_populates="tarea_asignaciones")
    desarrollador = relationship("Desarrollador", back_populates="tarea_asignaciones")
