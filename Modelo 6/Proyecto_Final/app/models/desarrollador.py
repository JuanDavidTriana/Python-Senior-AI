from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from .base import Base


class Desarrollador(Base):
    __tablename__ = 'desarrolladores'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)
    rol_scrum = Column(String(255), nullable=False)
    seniority = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    
    # Relationships
    desarrollador_proyectos = relationship("DesarrolladorProyecto", back_populates="desarrollador")
    desarrollador_habilidades = relationship("DesarrolladorHabilidad", back_populates="desarrollador")
    tarea_asignaciones = relationship("TareaAsignacion", back_populates="desarrollador")
