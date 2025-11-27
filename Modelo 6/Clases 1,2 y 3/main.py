from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()

@app.get("/")
def root():
    return {
        "mensaje": "Hola Mundo desde FastApi"
    }

@app.get("/usuarios/{id}")
def leer_usuario(id: int):
    return {
        "id":id,
        "nombre":"Juan"
        }