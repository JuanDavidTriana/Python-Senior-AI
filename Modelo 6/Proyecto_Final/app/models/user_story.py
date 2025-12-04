from sqlalchemy import Column, BigInteger, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class UserStory(Base):
    __tablename__ = 'user_stories'
    
    id = Column(BigInteger, primary_key=True)
    proyecto_id = Column(BigInteger, ForeignKey('proyectos.id'), nullable=False)
    sprint_id = Column(BigInteger, ForeignKey('spring.id'), nullable=False)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    prioridad = Column(String(255), nullable=False)
    puntos = Column(Integer, nullable=False)
    estado = Column(String(255), nullable=False)
    
    # Relationships
    proyecto = relationship("Proyecto", back_populates="user_stories")
    sprint = relationship("Sprint", back_populates="user_stories")
    tareas = relationship("Tarea", back_populates="user_story")
