from fastapi import FastAPI

from controller.vehiculoController import VehiculoController
from service.vehiculoService import vehiculoService
from repository.vehiculoRepository import VehiculoRepository

from controller.tipoVehiculoController import TipoVehiculoController
from service.tipoVehiculoService import tipoVehiculoService
from repository.tipoVehiculoRepository import TipoVehiculoRepository

from controller.pagoController import PagoController
from service.pagoService import pagoService
from repository.pagoRepository import PagoRepository


app =  FastAPI()

@app.get("/")
def root():
    return {
        "mensaje": "App parqueadero"
    }

# Inyección de dependencias
repository_vehiculo = VehiculoRepository()
service_vehiculo = vehiculoService(repository_vehiculo)
controller_vehiculo = VehiculoController(service_vehiculo)

tipo_vehiculo_repository = TipoVehiculoRepository()
tipo_vehiculo_service = tipoVehiculoService(tipo_vehiculo_repository)
tipo_vehiculo_controller = TipoVehiculoController(tipo_vehiculo_service)

pago_repository = PagoRepository()
pago_service = pagoService(pago_repository)
pago_controller = PagoController(pago_service)

app.include_router(controller_vehiculo.router)
app.include_router(tipo_vehiculo_controller.router)
app.include_router(pago_controller.router)