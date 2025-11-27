from fastapi import status, APIRouter
from service.tipoVehiculoService import tipoVehiculoService
from model.tipoVehiculos import TipoVehiculoCreate, TipoVehiculoUpdate, TipoVehiculo

class TipoVehiculoController:
    def __init__(self, service: tipoVehiculoService):
        #Inyección de la dependencia del servicio
        self.service = service

        #Router del controlador
        self.router = APIRouter(prefix="/tiposvehiculos", tags=["TiposVehiculos"])

        #Registro de rutas
        self.router.get("/")(self.listar_todos_tiposvehiculos)
        self.router.get("/activos")(self.listar_tiposvehiculos_activos)
        self.router.get("/{id_tipovehiculo}")(self.obtener_tipo_vehiculo_por_id)
        self.router.post("/", status_code=status.HTTP_201_CREATED)(self.crear_tipo_vehiculo)
        self.router.put("/{id_tipovehiculo}")(self.actualizar_tipo_vehiculo)
        self.router.patch("/cambiar-estado/{tipo_vehiculo_id}")(self.cambiar_estado_tipo_vehiculo)

    def listar_todos_tiposvehiculos(self):
        return self.service.listar_todos()
        
    def listar_tiposvehiculos_activos(self):
        return self.service.listar_activos()
    
    def obtener_tipo_vehiculo_por_id(self, id_tipovehiculo: int):
        return self.service.obtener_por_id(id_tipovehiculo)
    
    def crear_tipo_vehiculo(self, nombre:str, tarifa:float, limite:int):
        return self.service.crear(TipoVehiculoCreate(nombre=nombre, tarifa=tarifa, limite=limite))


    def actualizar_tipo_vehiculo(self, id_tipovehiculo: int, nombre:str, tarifa:float, limite:int, estado:bool):
        return self.service.actualizar(id_tipovehiculo, TipoVehiculoUpdate(nombre=nombre, tarifa=tarifa, limite=limite, estado=estado))
    
    def cambiar_estado_tipo_vehiculo(self, tipo_vehiculo_id: int):
        return self.service.cambiar_estado(tipo_vehiculo_id)
