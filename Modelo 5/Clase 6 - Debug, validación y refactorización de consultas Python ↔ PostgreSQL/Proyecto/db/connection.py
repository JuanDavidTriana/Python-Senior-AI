import psycopg2
from psycopg2 import OperationalError, Error
import os
from dotenv import load_dotenv

#Cargar variables desde archivo
load_dotenv()

DB_NAME= os.getenv("DB_NAME")
DB_USER= os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_HOST= os.getenv("DB_HOST")
DB_PORT= os.getenv("DB_PORT")

conn = None

def conectar():
    '''Establece una conexión a la base de datos PostgreSQL.'''
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexión exitosa a la base de datos.")
        return conn
    
    except (OperationalError, Error) as e:
        print(f"[ERROR] problema al conectar a la base de datos: {e}")

    return None

def cerrar_conexion(conn):
    '''Cierra la conexión a la base de datos PostgreSQL.'''
    if conn:
        conn.close()
        print("Conexión cerrada.")