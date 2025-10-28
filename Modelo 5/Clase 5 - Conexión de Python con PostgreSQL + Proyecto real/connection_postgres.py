"""
Script educativo para conectar Python con PostgreSQL usando psycopg2.

Incluye funciones para:
- Conectarse a la base de datos (conectar)
- Crear una tabla de ejemplo (crear_tabla)
- Insertar registros de forma segura (insertar_libro)
- Listar registros (mostrar_libros)

Características y buenas prácticas aplicadas:
- Manejo de errores con try/except y mensajes claros.
- Uso de parámetros (%s) para evitar inyección SQL.
- commit()/rollback() según corresponda.
- Cierre de recursos en finally (conexión) y context managers para cursores.

Requisitos:
- Instalar la librería psycopg2 (se recomienda psycopg2-binary para entorno local/desarrollo).
"""

from typing import Optional

import psycopg2
from psycopg2 import OperationalError, Error


def conectar(dbname: str, user: str, password: str, host: str = "localhost", port: int = 5432) -> Optional[psycopg2.extensions.connection]:
    """
    Establece la conexión con PostgreSQL y la devuelve.

    Parámetros:
        dbname: Nombre de la base de datos.
        user: Usuario de la base de datos.
        password: Contraseña del usuario.
        host: Host donde corre PostgreSQL (por defecto 'localhost').
        port: Puerto de conexión (por defecto 5432).

    Returns:
        Objeto conexión de psycopg2 si la conexión es exitosa; None si falla.
    """
    try:
        # Por defecto, autocommit está desactivado; así podemos controlar commit/rollback manualmente.
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        print(f"[OK] Conectado a PostgreSQL -> db='{dbname}', host='{host}', port={port}")
        return conn
    except OperationalError as oe:
        # OperationalError suele indicar problemas de red, credenciales o disponibilidad del servidor.
        print("[ERROR] No se pudo establecer la conexión con PostgreSQL (OperationalError):", oe)
    except Error as e:
        # Cualquier otro error específico de psycopg2.
        print("[ERROR] Fallo general de psycopg2 al conectar:", e)
    except Exception as ex:
        # Errores no esperados.
        print("[ERROR] Error inesperado al conectar:", ex)
    # Si hubo error, devolvemos None.
    return None


def crear_tabla(conn: psycopg2.extensions.connection) -> None:
    """
    Crea la tabla 'libros' si no existe.

    Esquema:
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(100),
        autor VARCHAR(100),
        anio INT
    """
    sql_ddl = (
        """
        CREATE TABLE IF NOT EXISTS libros (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            anio INT
        );
        """
    )

    try:
        # Usamos un context manager para cerrar el cursor automáticamente.
        with conn.cursor() as cur:
            cur.execute(sql_ddl)
        conn.commit()
        print("[OK] Tabla 'libros' verificada/creada.")
    except Error as e:
        # Si ocurre un error, revertimos cambios.
        conn.rollback()
        print("[ERROR] No se pudo crear/verificar la tabla 'libros':", e)
        # No relanzamos para permitir que el flujo principal decida continuar o no.


def insertar_libro(conn: psycopg2.extensions.connection, titulo: str, autor: str, anio: int) -> None:
    """
    Inserta un libro en la tabla 'libros' usando parámetros seguros (%s) para evitar inyección SQL.

    Parámetros:
        titulo: Título del libro.
        autor: Autor del libro.
        anio: Año de publicación (entero).
    """
    sql_insert = "INSERT INTO libros (titulo, autor, anio) VALUES (%s, %s, %s);"

    try:
        with conn.cursor() as cur:
            # Los valores van en una tupla, psycopg2 se encarga de escapar correctamente.
            cur.execute(sql_insert, (titulo, autor, anio))
        conn.commit()
        print(f"[OK] Libro insertado: '{titulo}' de {autor} ({anio}).")
    except Error as e:
        conn.rollback()
        print("[ERROR] No se pudo insertar el libro:", e)


def mostrar_libros(conn: psycopg2.extensions.connection) -> None:
    """
    Recupera y muestra todos los registros de la tabla 'libros'.
    """
    sql_select = "SELECT id, titulo, autor, anio FROM libros ORDER BY id;"

    try:
        with conn.cursor() as cur:
            cur.execute(sql_select)
            filas = cur.fetchall()

        if not filas:
            print("[INFO] No hay libros registrados aún.")
            return

        print("\nListado de libros:")
        print("-" * 60)
        for (id_libro, titulo, autor, anio) in filas:
            print(f"#{id_libro:>3} | {titulo:<30} | {autor:<25} | {anio}")
        print("-" * 60)
    except Error as e:
        print("[ERROR] No se pudieron recuperar los libros:", e)


if __name__ == "__main__":
    """
    Flujo principal de demostración:
    1) Conecta a la base de datos 'biblioteca'.
    2) Crea la tabla 'libros' si no existe.
    3) Inserta un libro de prueba.
    4) Muestra todos los libros.

    NOTA: Ajusta las credenciales según tu entorno local.
    """
    # Ajusta estas credenciales a tu entorno local
    DB_NAME = "biblioteca"  # Asegúrate de que esta BD exista
    DB_USER = "postgres"    # Usuario por defecto en instalaciones locales
    DB_PASSWORD = "tu_password"  # Cambia por tu contraseña real
    DB_HOST = "localhost"
    DB_PORT = 5432

    conn = None
    try:
        conn = conectar(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
        if conn is None:
            # Si no hay conexión, detenemos la ejecución de forma segura.
            raise SystemExit("No se pudo conectar a la base de datos. Verifica credenciales y disponibilidad del servidor.")

        # 1) Crear/verificar tabla
        crear_tabla(conn)

        # 2) Insertar un libro de prueba (puedes cambiar estos valores)
        insertar_libro(conn, "Cien años de soledad", "Gabriel García Márquez", 1967)

        # 3) Mostrar todos los libros
        mostrar_libros(conn)

    except SystemExit as se:
        # Mensaje ya informativo; solo lo mostramos.
        print(se)
    except Exception as ex:
        # Captura de seguridad para cualquier otro error no previsto.
        print("[ERROR] Ocurrió un problema durante la ejecución:", ex)
    finally:
        # Cerrar la conexión SIEMPRE si fue abierta.
        try:
            if conn is not None and not getattr(conn, "closed", 1):  # closed==0 cuando está abierta
                conn.close()
                print("[OK] Conexión cerrada correctamente.")
        except Exception as ex_close:
            print("[WARN] No se pudo cerrar la conexión limpiamente:", ex_close)
