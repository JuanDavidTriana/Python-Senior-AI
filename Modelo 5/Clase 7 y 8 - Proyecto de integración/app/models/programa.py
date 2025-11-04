from dataclasses import dataclass

@dataclass
class Programa:
    id: int | None
    nombre: str
    duracion: int # En minutos
    docente_id: int