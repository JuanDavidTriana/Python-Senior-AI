from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema para un desarrollador
class DeveloperSchema(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str
    rol_scrum: str
    seniority: str
    estado: str

class DeveloperCreateSchema(DeveloperSchema):
    pass

class DeveloperUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    rol_scrum: Optional[str] = None
    seniority: Optional[str] = None
    estado: Optional[str] = None

class DeveloperResponseSchema(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    telefono: str
    rol_scrum: str
    seniority: str
    estado: str

    class Config:
        orm_mode = True
    