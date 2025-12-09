from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.orm import relationship
from .base import Base


class Proyecto(Base):
    __tablename__ = 'proyectos'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    product_owner_id = Column(BigInteger, nullable=False)
    scrum_master_id = Column(BigInteger, nullable=False)
    
    # Relationships
    sprints = relationship("Sprint", back_populates="proyecto")
    user_stories = relationship("UserStory", back_populates="proyecto")
    desarrollador_proyectos = relationship("DesarrolladorProyecto", back_populates="proyecto")
