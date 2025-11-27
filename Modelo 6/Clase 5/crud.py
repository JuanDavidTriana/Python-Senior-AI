from sqlalchemy.orm import Session
from cliente import Cliente # Modelo 
from schema import ClienteCreate # Esquema de Pydantic

def crear(db: Session, cliente: ClienteCreate):
    nuevoCliente = Cliente(
        nombre= cliente.nombre,
        edad= cliente.edad,
        img_url = cliente.img_url
    )
    db.add(nuevoCliente)
    db.commit()
    db.refresh(nuevoCliente)
    return nuevoCliente

def leer(db:Session):
    return db.query(Cliente).all()