from datetime import datetime
'''
class TipoVehiculo:
    id: int | None = None
    nombre: str = ''
    tarifa: float = 0.0
    limite: int = 0
    createdAt: datetime | None = None
'''
class TipoVehiculo:
    def __init__(self,id,nombre,tarifa,limite,createdAt):
        self.id = id
        self.nombre = nombre
        self.tarifa = tarifa
        self.limite = limite
        self.createdAt = createdAt

    def validate(self):
        if self.tarifa <= 0.0:
            raise ValueError("La tarifa no puede ser 0 o negativo")
        if self.limite <= 0.0:
            raise ValueError("El limite de puede ser igual o inferior a 0")
        if len(self.nombre) > 100:
            raise ValueError("El nombre no puede tener mas de 100 caracteres")