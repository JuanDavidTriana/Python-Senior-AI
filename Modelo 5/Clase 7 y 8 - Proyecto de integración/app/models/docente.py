from dataclasses import dataclass

@dataclass
class Docentes:
    id: int | None
    nombre: str
    correo: str

