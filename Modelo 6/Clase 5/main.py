from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from cliente import Cliente
from schema import ClienteCreate
from crud import crear, leer

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

Base.metadata.create_all(bind=engine)

@app.post("/clientes")
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return crear(db, cliente)

@app.get("/cliente")
def llamar_clientes(db: Session = Depends(get_db)):
    return leer(db)