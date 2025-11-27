from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import cliente, clienteController, schemas
from database import get_db, Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    return clienteController.get_clientes(db)
