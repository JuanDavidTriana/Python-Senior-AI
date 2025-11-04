import os 
from contextlib import contextmanager


from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError

load_dotenv()


def get_db_params() -> dict:
    return {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }

@contextmanager
def get_connection():
    conn = psycopg2.connect(**get_db_params())
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise 
    finally:
        conn.close()

def health_check():
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
    
