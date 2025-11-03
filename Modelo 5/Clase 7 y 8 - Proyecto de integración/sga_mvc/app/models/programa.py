from dataclasses import dataclass


@dataclass
class Programa:
    id: int | None
    nombre: str
    duracion: int  # en horas o créditos
    docente_id: int | None
