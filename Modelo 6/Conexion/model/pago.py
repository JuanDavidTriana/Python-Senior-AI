from pydantic import BaseModel, Field
from datetime import datetime

class Pago(BaseModel):
    id: int
    vehiculo_id: int
    pago: float
    created_at: datetime

class PagoCreate(BaseModel):
    vehiculo_id: int = Field(..., gt=0)
    pago: float = Field(..., gt=0)