from fastapi import FastAPI

from controller.controllerCliente import ClienteController

app = FastAPI()

cliente_controller = ClienteController()

app.include_router(cliente_controller.router)