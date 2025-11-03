from typing import List, Optional

from app.db.connection import get_connection
from app.models.nota import Nota


class NotaRepository:
    @staticmethod
    def create(alumno_id: int, asignatura: str, calificacion: float) -> Nota:
        sql = "INSERT INTO notas(alumno_id, asignatura, calificacion) VALUES (%s, %s, %s) RETURNING id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (alumno_id, asignatura, calificacion))
                new_id = cur.fetchone()[0]
                return Nota(id=new_id, alumno_id=alumno_id, asignatura=asignatura, calificacion=calificacion)

    @staticmethod
    def get_by_id(nota_id: int) -> Optional[Nota]:
        sql = "SELECT id, alumno_id, asignatura, calificacion FROM notas WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nota_id,))
                row = cur.fetchone()
                if not row:
                    return None
                return Nota(id=row[0], alumno_id=row[1], asignatura=row[2], calificacion=float(row[3]))

    @staticmethod
    def get_all_by_alumno(alumno_id: int) -> List[Nota]:
        sql = "SELECT id, alumno_id, asignatura, calificacion FROM notas WHERE alumno_id = %s ORDER BY id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (alumno_id,))
                rows = cur.fetchall()
                return [Nota(id=r[0], alumno_id=r[1], asignatura=r[2], calificacion=float(r[3])) for r in rows]

    @staticmethod
    def update(nota_id: int, asignatura: str, calificacion: float) -> bool:
        sql = "UPDATE notas SET asignatura=%s, calificacion=%s WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (asignatura, calificacion, nota_id))
                return cur.rowcount > 0

    @staticmethod
    def delete(nota_id: int) -> bool:
        sql = "DELETE FROM notas WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nota_id,))
                return cur.rowcount > 0
