from service.pagoService import pagoService
from fastapi import status, APIRouter, HTTPException

class PagoController:
    def __init__(self, service: pagoService):
        self.service = service

        self.router = APIRouter(prefix="/pagos", tags=["Pagos"])

        self.router.get("/")(self.obtener_pagos)

    def obtener_pagos(self):
        try:
            pagos = self.service.obtener_pagos()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        return pagos