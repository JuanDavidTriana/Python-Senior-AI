from typing import List
from fastapi import status, APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from service.vehiculoService import vehiculoService
from schema.vehiculos import VehiculoCreate, Vehiculo, VehiculoCreatedResponse
from repository.vehiculoRepository import VehiculoRepository
from database.database import get_connection


class VehiculoController:
    def __init__(self):

        #Router del controlador
        self.router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

        #Registro de rutas
        self.router.get("/", response_model=List[Vehiculo])(self.listar_vehiculos)
        self.router.post("/", status_code=status.HTTP_201_CREATED, response_model=VehiculoCreatedResponse)(self.crear_vehiculo)

    def _get_service(self, db: Session = Depends(get_connection)) -> vehiculoService:
        repository = VehiculoRepository(db)
        return vehiculoService(repository)

    def listar_vehiculos(self, service: vehiculoService = Depends(_get_service)):
        try:
            vehiculos = service.listar()
            # Map ORM objects to Pydantic schema instances (estado no existe en ORM, asumimos True)
            return [Vehiculo(
                id=v.id,
                id_tipovehiculo=v.id_tipovehiculo,
                placa=v.placa,
                documento=v.documento,
                nombre=v.nombre,
                hora_llegada=v.hora_llegada,
                estado=True
            ) for v in vehiculos]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def crear_vehiculo(self, data: VehiculoCreate, service: vehiculoService = Depends(_get_service)):
        try:
            return service.crear(data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    