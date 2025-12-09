from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from utils.database import init_db
from routers import developer


# Import all models to ensure they are registered with SQLAlchemy
from models.desarrollador import Desarrollador
from models.desarrollador_proyecto import DesarrolladorProyecto
from models.desarrollador_habilidad import DesarrolladorHabilidad
from models.proyecto import Proyecto
from models.habilidad import Habilidad
from models.spring import Sprint
from models.tarea import Tarea
from models.tarea_asignacion import TareaAsignacion
from models.user_story import UserStory


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="API Gesion de proyectos Scrum",
    description="API para gestionar proyectos Scrum, desarrolladores, sprints y tareas.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir todas las origines 
    allow_credentials=True, # Permitir el uso de cookies
    allow_methods=["*"], # Permitir todos los métodos HTTP
    allow_headers=["*"], # Permitir todas las cabeceras
)

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Welcome to the API Gesion de proyectos Scrum",
            "version": "1.0.0",
            "documentation": "/docs"
            }

app.include_router(developer.router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)