from pathlib import Path
from app.db.connection import get_connection


def init_schema() -> None:
    schema_path = Path(__file__).with_name("schema.sql")
    sql = schema_path.read_text(encoding="utf-8")
    # Ejecutar cada sentencia separada por punto y coma que no esté vacía
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    with get_connection() as conn:
        with conn.cursor() as cur:
            for st in statements:
                cur.execute(st)
