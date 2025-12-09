from sqlalchemy import Column, BigInteger, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Tarea(Base):
    __tablename__ = 'tareas'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_story_id = Column(BigInteger, ForeignKey('user_stories.id'), nullable=False)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    horas_estimadas = Column(DateTime, nullable=True)
    horas_restantes = Column(DateTime, nullable=False)
    estado = Column(String(255), nullable=False)
    
    # Relationships
    user_story = relationship("UserStory", back_populates="tareas")
    tarea_asignaciones = relationship("TareaAsignacion", back_populates="tarea")
