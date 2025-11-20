from fastapi import status, APIRouter, HTTPException 
from service.vehiculoService import vehiculoService
from model.vehiculos import VehiculoCreate


class VehiculoController:
    def __init__(self, service: vehiculoService):
        #Inyección de la dependencia del servicio
        self.service = service

        #Router del controlador
        self.router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

        #Registro de rutas
        self.router.get("/")(self.listar_vehiculos)
        self.router.post("/", status_code=status.HTTP_201_CREATED)(self.crear_vehiculo)
        self.router.patch("/{vehiculo_id}")(self.cambiar_estado_vehiculo)
        self.router.put("/{id_vehiculo}")(self.actualizar_vehiculos)
        self.router.delete("/{vehiculo_id}")(self.eliminar_vehiculo)

    def listar_vehiculos(self):
        try:
            return self.service.listar()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def crear_vehiculo(self, tipoVehiculo:int,placa:str,documento:str,nombre:str):
        try:
            return self.service.crear(VehiculoCreate(tipoVehiculo=tipoVehiculo, placa=placa, documento=documento, nombre=nombre))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def cambiar_estado_vehiculo(self,vehiculo_id: str):
        try:
            return self.service.cambiar_estado(vehiculo_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def actualizar_vehiculos(self, id_vehiculo: int, id_tipovehiculo: int, placa: str, documento: str, nombre: str, estado: bool):
        try:
            return self.service.actualizar(id_vehiculo, id_tipovehiculo, placa, documento, nombre, estado)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def eliminar_vehiculo(self, vehiculo_id: int):
        try:
            return self.service.eliminar(vehiculo_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))