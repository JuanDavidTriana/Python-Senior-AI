from fastapi import HTTPException 
from repository.vehiculoRepository import VehiculoRepository
from schema.vehiculos import VehiculoCreate

class vehiculoService:
    def __init__(self, repository: VehiculoRepository):
        self.repository = repository

    def listar(self):
        return self.repository.listar()
    
    def cambiar_estado(self, vehiculo_id: str):
        result = self.repository.cambiar_estado(vehiculo_id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Vehiculo con id {vehiculo_id} no encontrado.")
        self.repository.db.commit()
        return {"id": vehiculo_id, "nuevo_estado": result["estado"]}
    
    def crear(self, model: VehiculoCreate):
        vehiculo_id = self.repository.crear(model.tipoVehiculo, model.placa, model.documento, model.nombre)
        self.repository.db.commit()
        return {"id": vehiculo_id}
    
    def actualizar(self, id_vehiculo: int, id_tipovehiculo: int, placa: str, documento: str, nombre: str, estado: bool):
        updated_vehiculo = self.repository.actualizar(id_vehiculo, id_tipovehiculo, placa, documento, nombre, estado)

        if updated_vehiculo is None:
            raise HTTPException(status_code=404, detail=f"Vehiculo con id {id_vehiculo} no encontrado.")

        self.repository.db.commit()
        return updated_vehiculo
    
    def eliminar(self, vehiculo_id: int):
        result = self.repository.eliminar(vehiculo_id)

        if result is None:
            raise HTTPException(status_code=404, detail=f"Vehiculo con id {vehiculo_id} no encontrado.")
        
        self.repository.db.commit()
        return {"mensaje": f"Vehiculo con id {vehiculo_id} eliminado correctamente."}