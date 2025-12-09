from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

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

# Configurar la conexión a la base de datos PostgreSQL
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_base_datos
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/scrum_db"
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión
Session = sessionmaker(bind=engine)

def get_db():
    """Generador de sesión de base de datos"""
    db = Session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Inicializar la base de datos creando todas las tablas"""
    Base.metadata.create_all(bind=engine)
