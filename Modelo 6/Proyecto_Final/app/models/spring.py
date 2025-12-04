from sqlalchemy import Column, BigInteger, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Sprint(Base):
    __tablename__ = 'spring'
    
    id = Column(BigInteger, primary_key=True)
    proyecto_id = Column(BigInteger, ForeignKey('proyectos.id'), nullable=False)
    nombre = Column(String(255), nullable=False)
    objetivo = Column(Text, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    estado = Column(String(255), nullable=False)
    
    # Relationships
    proyecto = relationship("Proyecto", back_populates="sprints")
    user_stories = relationship("UserStory", back_populates="sprint")
