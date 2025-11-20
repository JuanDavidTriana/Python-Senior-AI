import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="parqueadero",
        user="postgres",
        password="admin",
        port=5432,
        cursor_factory= RealDictCursor # Para obtener diccionarios en lugar de tupas

    )
    return conn