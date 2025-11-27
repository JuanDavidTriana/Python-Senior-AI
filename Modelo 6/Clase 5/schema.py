from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre: str
    edad: int
    img_url: str
    