from repository.pagoRepository import PagoRepository
from fastapi import HTTPException
from model.pago import Pago

class pagoService:
    def __init__(self, repository: PagoRepository):
        self.repository = repository

    def obtener_pagos(self):
        return self.repository.obtener_pagos()
