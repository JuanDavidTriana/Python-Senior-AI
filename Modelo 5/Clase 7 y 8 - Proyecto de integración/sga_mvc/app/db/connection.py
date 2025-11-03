from __future__ import annotations
import os
from contextlib import contextmanager
from typing import Iterator

from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError


load_dotenv()


def get_db_params() -> dict:
    """Retorna los parámetros de conexión a la base de datos."""
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "5432")),
        "dbname": os.getenv("DB_NAME", "sga_mvc"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "admin"),
    }


@contextmanager
def get_connection() -> Iterator[psycopg2.extensions.connection]:
    """Context manager para obtener una conexión a la base de datos."""
    conn = psycopg2.connect(**get_db_params())
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def health_check() -> bool:
    """Verifica si la conexión a la base de datos está disponible."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        return True
    except OperationalError:
        return False
    except Exception:
        return False
