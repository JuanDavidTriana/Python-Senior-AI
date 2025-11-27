from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    ciudad: str
    edad: int