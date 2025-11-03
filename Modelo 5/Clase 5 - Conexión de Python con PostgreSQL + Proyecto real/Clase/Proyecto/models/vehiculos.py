from datetime import datetime

class Vehiculo:
    def __init__(self,id, idTipoVehiculo, placa, documento, nombre, horaIngreso, estado, createdAt):
        self.id = id
        self.idTipoVehiculo = idTipoVehiculo
        self.placa = placa
        self.documento = documento
        self.nombre = nombre
        self.horaIngreso = horaIngreso
        self.estado = estado
        self.createdAt = createdAt

    def validate(self):
        if len(self.placa) > 10:
            raise ValueError("La placa no puede tener mas de 10 caracteres")
        if len(self.documento) > 20:
            raise ValueError("El documento no puede tener mas de 20 caracteres")
        if len(self.nombre) > 100:
            raise ValueError("El nombre no puede tener mas de 100 caracteres")