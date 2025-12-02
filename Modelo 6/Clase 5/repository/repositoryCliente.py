from sqlalchemy.orm import Session
from model.cliente import Cliente # Modelo 
from schema.schema import ClienteCreate, ClienteUpdate # Esquema de Pydantic

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

def leer_por_id(db:Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def leer_cliente_letra(db:Session, letra: str):
    return db.query(Cliente).filter(Cliente.nombre.ilike(f'%{letra}%')).all()

def actualizar(db:Session, cliente_id: int, cliente: ClienteUpdate):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente_db:
        return None

    cliente_db.nombre = cliente.nombre
    cliente_db.edad = cliente.edad
    cliente_db.img_url = cliente.img_url

    db.commit()
    db.refresh(cliente_db)
    return cliente_db

def eliminar(db:Session, cliente_id: int):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente_db:
        return None
    
    db.delete(cliente_db)
    db.commit()
    return cliente_db