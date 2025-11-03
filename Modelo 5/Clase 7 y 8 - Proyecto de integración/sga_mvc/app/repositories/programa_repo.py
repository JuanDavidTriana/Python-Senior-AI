from typing import List, Optional

from app.db.connection import get_connection
from app.models.programa import Programa


class ProgramaRepository:
    @staticmethod
    def create(nombre: str, duracion: int, docente_id: int | None) -> Programa:
        sql = "INSERT INTO programas(nombre, duracion, docente_id) VALUES (%s, %s, %s) RETURNING id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre, duracion, docente_id))
                new_id = cur.fetchone()[0]
                return Programa(id=new_id, nombre=nombre, duracion=duracion, docente_id=docente_id)

    @staticmethod
    def get_by_id(programa_id: int) -> Optional[Programa]:
        sql = "SELECT id, nombre, duracion, docente_id FROM programas WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (programa_id,))
                row = cur.fetchone()
                if not row:
                    return None
                return Programa(id=row[0], nombre=row[1], duracion=row[2], docente_id=row[3])

    @staticmethod
    def get_all() -> List[Programa]:
        sql = "SELECT id, nombre, duracion, docente_id FROM programas ORDER BY id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                return [Programa(id=r[0], nombre=r[1], duracion=r[2], docente_id=r[3]) for r in rows]

    @staticmethod
    def update(programa_id: int, nombre: str, duracion: int, docente_id: int | None) -> bool:
        sql = "UPDATE programas SET nombre=%s, duracion=%s, docente_id=%s WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre, duracion, docente_id, programa_id))
                return cur.rowcount > 0

    @staticmethod
    def delete(programa_id: int) -> bool:
        sql = "DELETE FROM programas WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (programa_id,))
                return cur.rowcount > 0
