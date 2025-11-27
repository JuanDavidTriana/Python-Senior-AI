from sqlalchemy.orm import Session
from interfaces.iVehiculo import InterfaceVehiculo
from model.orm_models import VehiculoORM

class VehiculoRepository(InterfaceVehiculo):
    def __init__(self, db: Session):
        self.db = db
        
    def listar(self):
        return self.db.query(VehiculoORM).all()
    
    def crear(self, tipoVehiculo:int,placa:str,documento:str,nombre:str):
        nuevo_vehiculo = VehiculoORM(
            id_tipovehiculo= tipoVehiculo,
            placa= placa,
            documento= documento,
            nombre= nombre
        )
        self.db.add(nuevo_vehiculo)
        self.db.flush() # Asegura que el ID se genere
        return nuevo_vehiculo.id
    
    