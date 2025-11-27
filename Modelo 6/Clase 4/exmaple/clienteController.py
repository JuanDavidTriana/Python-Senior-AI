from sqlalchemy.orm import Session
import cliente, schemas

def get_clientes(db: Session):
    return db.query(cliente.Cliente).all()