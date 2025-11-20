from pydantic import BaseModel, Field
from datetime import datetime

# Modelo para llamar uno o varios tipos de vehículos (GET)
class TipoVehiculo(BaseModel):
    id: int
    nombre: str
    tarifa: float
    limite: int
    estado: bool

# Modelo para crear un tipo de vehículo (POST)
class TipoVehiculoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    tarifa: float = Field(..., gt=0)
    limite: int = Field(..., gt=0)

# Modelo para actualizar un tipo de vehículo (PUT)
class TipoVehiculoUpdate(BaseModel):
    nombre: str
    tarifa: float
    limite: int
    estado: bool

