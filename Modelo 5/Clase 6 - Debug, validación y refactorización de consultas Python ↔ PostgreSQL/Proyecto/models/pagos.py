from datetime import datetime

class Pago:
    def __init__(self,id, idVehiculo,pago, createAt):
        self.id = id
        self.idVehiculo = idVehiculo
        self.pago = pago
        self.createAt = createAt

    def validate(self):
        if self.pago < 0:
            raise ValueError("El pago no puede ser negativo")