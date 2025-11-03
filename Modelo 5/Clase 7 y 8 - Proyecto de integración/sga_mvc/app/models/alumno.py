from dataclasses import dataclass


@dataclass
class Alumno:
    id: int | None
    nombre: str
    correo: str
    programa_id: int
