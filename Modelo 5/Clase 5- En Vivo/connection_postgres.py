import psycopg2
from psycopg2 import OperationalError, Error
import os
from dotenv import load_dotenv

#Cargar variables desde archivo
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER") #Nombre de usuario
DB_PASSWORD = os.getenv("DB_PASSWORD") #Password de su base de datos
DB_HOST = os.getenv("DB_HOST") # 127.0.0.1
DB_PORT = os.getenv("DB_PORT")



conn = None

def conectar():
    try:
        conn = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT
        )
        print('Conexion OK')
        return conn
    except OperationalError as oe:
        print(f'[Error] Problema operacional al conectar: {oe}')
    except Error as e:
        print(f'[Error] psycopg2 Error al conectar: {e}')
    except Exception as ex:
        print(f'[Error] Inesperado: {ex}')

    return None



def llamar_profesores(conn: psycopg2.extensions.connection):

    query = '''SELECT * FROM school.teachers'''

    try:
        with conn.cursor() as cur:
            cur.execute(query)
            filas = cur.fetchall()

        if not filas:
            print(f'[INFO] No hay profesores.')
            return

        for name in filas:
            print(name)
    except Error as e:
        print(f'[Error] No se pudieron recuperar los profesores: {e}')


def ingresar_profesor(conn: psycopg2.extensions.connection,id_departamento,nombre,apellido,email,telefono,salario):
    
    query = '''INSERT INTO school.teachers(department_id,first_name,last_name,email,phone,salary) 
    VALUES (%s,%s,%s,%s,%s,%s)'''
    try:
        with conn.cursor() as cur:
            cur.execute(query,(id_departamento,nombre,apellido,email,telefono,salario))
        conn.commit()
        print('[OK] Insercion segura registrada')
    except Error as e:
        conn.rollback()
        print(f'[Error] Insercion segura fallo: {e}')

conn = conectar()
if conn is None:
    print(f'[Error] No se pudo contectar a la base de datos')
#llamar_profesores(conn)
ingresar_profesor(conn,1,'Juan David','Triana','jtrianxa@devseniorcode.com','320920',50000)
