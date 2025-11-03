from dataclasses import dataclass


@dataclass
class Docente:
    id: int | None
    nombre: str
    correo: str
