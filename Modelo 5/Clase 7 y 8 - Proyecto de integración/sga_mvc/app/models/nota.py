from dataclasses import dataclass


@dataclass
class Nota:
    id: int | None
    alumno_id: int
    asignatura: str
    calificacion: float
