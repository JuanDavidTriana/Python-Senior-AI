from pydantic import BaseModel, Field
from datetime import datetime

#Modelo para crear un vehículo(POST)
class VehiculoCreate(BaseModel):
    tipoVehiculo: int = Field(..., description="ID del tipo de vehículo")
    placa: str = Field(..., min_length=3, max_length=7)
    documento: str = Field(..., min_length=5, max_length=20)
    nombre: str = Field(..., min_length=2, max_length=100)

#Modelo para actualizar un vehículo(PUT)
class VehiculoUpdate(BaseModel):
    id_tipovehiculo: int 
    placa: str 
    documento: str
    nombre: str
    estado: bool 

#Modelo para representar un vehículo (GET)
class Vehiculo(BaseModel):
    id: int
    id_tipovehiculo: int
    placa: str
    documento: str
    nombre: str
    hora_llegada: datetime
    estado: bool

class VehiculoCreatedResponse(BaseModel):
    id: int