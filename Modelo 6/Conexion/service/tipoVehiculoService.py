from repository.tipoVehiculoRepository import TipoVehiculoRepository
from fastapi import HTTPException
from model.tipoVehiculos import TipoVehiculoCreate, TipoVehiculoUpdate, TipoVehiculo

class tipoVehiculoService:
    def __init__(self, repository: TipoVehiculoRepository):
        self.repository = repository

    def listar_todos(self):
        return self.repository.listarTodos()
    
    def listar_activos(self):
        return self.repository.listarActivos()
    
    def obtener_por_id(self, id_tipovehiculo: int):
        tipo_vehiculo = self.repository.obtenerPorId(id_tipovehiculo)
        if tipo_vehiculo is None:
            raise HTTPException(status_code=404, detail=f"Tipo de Vehiculo con id {id_tipovehiculo} no encontrado.")
        return tipo_vehiculo
    
    def crear(self, model: TipoVehiculoCreate):
        tipo_vehiculo_id = self.repository.crear(model.nombre, model.tarifa, model.limite)
        self.repository.conn.commit()
        return {"id": tipo_vehiculo_id}
    
    def actualizar(self, id_tipovehiculo: int, model: TipoVehiculoUpdate):
        updated_tipo_vehiculo = self.repository.actualizar(id_tipovehiculo, model.nombre, model.tarifa, model.limite, model.estado)

        if updated_tipo_vehiculo is None:
            raise HTTPException(status_code=404, detail=f"Tipo de Vehiculo con id {id_tipovehiculo} no encontrado.")

        self.repository.conn.commit()
        return updated_tipo_vehiculo
    
    def cambiar_estado(self, tipo_vehiculo_id: int):
        result = self.repository.cambiarEstado(tipo_vehiculo_id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Tipo de Vehiculo con id {tipo_vehiculo_id} no encontrado.")
        self.repository.conn.commit()
        return {"id": tipo_vehiculo_id, "nuevo_estado": result["estado"]}