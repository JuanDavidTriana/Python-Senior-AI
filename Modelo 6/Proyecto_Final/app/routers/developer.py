from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.desarrollador import Desarrollador
from schemas.schemas import DeveloperCreateSchema, DeveloperUpdateSchema, DeveloperResponseSchema
from utils.database import get_db
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix="/api/developers",
    tags=["Developers"]
)

class EstadosEnumeration(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    VACACIONES = "Vacaciones"

@router.get("/", response_model=list[DeveloperResponseSchema])
def list_developers(db: Session = Depends(get_db)):
    developers = db.query(Desarrollador).filter(Desarrollador.estado == "Activo").all()
    return developers

@router.get("/all", response_model=list[DeveloperResponseSchema])
def list_all_developers(db: Session = Depends(get_db)):
    developers = db.query(Desarrollador).all()
    return developers

@router.get("/developers", response_model=list[DeveloperResponseSchema])
def list_developers_all_alternate(
    estado: Optional[EstadosEnumeration] = None, 
    limit: int = 10, 
    db: Session = Depends(get_db)):
    if estado is None:
        developers = db.query(Desarrollador).all()
    else:
        developers = db.query(Desarrollador).filter(Desarrollador.estado == estado).limit(limit).all()
    return developers

@router.get("/{developer_id}", response_model=DeveloperResponseSchema)
def get_developer(developer_id: int, db: Session = Depends(get_db)):
    developer = db.query(Desarrollador).filter(Desarrollador.id == developer_id).first()
    if not developer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    return developer

@router.post("/", response_model=DeveloperResponseSchema, status_code=status.HTTP_201_CREATED)
def create_developer(developer: DeveloperCreateSchema, db: Session = Depends(get_db)):
    new_developer = Desarrollador(
        nombre=developer.nombre,
        apellido=developer.apellido,
        correo=developer.correo,
        telefono=developer.telefono,
        rol_scrum=developer.rol_scrum,
        seniority=developer.seniority,
        estado=developer.estado
    )
    db.add(new_developer)
    db.commit()
    db.refresh(new_developer)
    return new_developer

@router.put("/{developer_id}", response_model=DeveloperResponseSchema)
def update_developer(developer_id: int, developer_update: DeveloperUpdateSchema, db: Session = Depends(get_db)):
    developer = db.query(Desarrollador).filter(Desarrollador.id == developer_id).first()
    if not developer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    for var, value in vars(developer_update).items():
        if value is not None:
            setattr(developer, var, value)
    
    db.commit()
    db.refresh(developer)
    return developer

# No es común usar DELETE en REST para desactivar un recurso
@router.delete("/{developer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_developer(developer_id: int, db: Session = Depends(get_db)):
    developer = db.query(Desarrollador).filter(Desarrollador.id == developer_id).first()
    if not developer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    db.delete(developer)
    db.commit()
    return None

@router.put("/cambiar_estado/{developer_id}", response_model=DeveloperResponseSchema)
def change_developer_status(developer_id: int, db: Session = Depends(get_db)):
    developer = db.query(Desarrollador).filter(Desarrollador.id == developer_id).first()
    if not developer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    developer.estado = "Inactivo" if developer.estado != "Inactivo" else "Activo"
    db.commit()
    db.refresh(developer)
    return developer

@router.put("/cambiar_estado2/{developer_id}", response_model=DeveloperResponseSchema)
def change_developer_status_alternate(developer_id: int, estado: Optional[EstadosEnumeration], db: Session = Depends(get_db)):
    developer = db.query(Desarrollador).filter(Desarrollador.id == developer_id).first()
    if not developer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    developer.estado = estado.value
    db.commit()
    db.refresh(developer)
    return developer