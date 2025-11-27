import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


uri = "postgresql+psycopg2://postgres:admin@localhost:5432/academiaPython"

# Crear el motor de la base de datos
engine = create_engine(uri, echo=True, future=True)

# Crear una sesión
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

# Crear la clase base para los modelos
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()