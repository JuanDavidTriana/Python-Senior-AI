from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from controller.vehiculoController import VehiculoController
from service.vehiculoService import vehiculoService
from repository.vehiculoRepository import VehiculoRepository

from database.database import get_connection, engine, Base

Base.metadata.create_all(bind=engine)

app =  FastAPI()

@app.get("/")
def root():
    return {
        "mensaje": "App parqueadero"
    }

def get_vehiculo_service(db: Session = Depends(get_connection)):
    repository = VehiculoRepository(db)
    return vehiculoService(repository)

app.dependency_overrides[vehiculoService] = get_vehiculo_service

controller_vehiculo = VehiculoController()


app.include_router(controller_vehiculo.router)
