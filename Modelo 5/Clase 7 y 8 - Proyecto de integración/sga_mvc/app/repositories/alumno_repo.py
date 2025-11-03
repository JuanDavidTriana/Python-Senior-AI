from typing import List, Optional

from app.db.connection import get_connection
from app.models.alumno import Alumno


class AlumnoRepository:
    @staticmethod
    def create(nombre: str, correo: str, programa_id: int) -> Alumno:
        sql = "INSERT INTO alumnos(nombre, correo, programa_id) VALUES (%s, %s, %s) RETURNING id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre, correo, programa_id))
                new_id = cur.fetchone()[0]
                return Alumno(id=new_id, nombre=nombre, correo=correo, programa_id=programa_id)

    @staticmethod
    def get_by_id(alumno_id: int) -> Optional[Alumno]:
        sql = "SELECT id, nombre, correo, programa_id FROM alumnos WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (alumno_id,))
                row = cur.fetchone()
                if not row:
                    return None
                return Alumno(id=row[0], nombre=row[1], correo=row[2], programa_id=row[3])

    @staticmethod
    def get_by_email(correo: str) -> Optional[Alumno]:
        sql = "SELECT id, nombre, correo, programa_id FROM alumnos WHERE correo = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (correo,))
                row = cur.fetchone()
                if not row:
                    return None
                return Alumno(id=row[0], nombre=row[1], correo=row[2], programa_id=row[3])

    @staticmethod
    def get_all() -> List[Alumno]:
        sql = "SELECT id, nombre, correo, programa_id FROM alumnos ORDER BY id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                return [Alumno(id=r[0], nombre=r[1], correo=r[2], programa_id=r[3]) for r in rows]

    @staticmethod
    def update(alumno_id: int, nombre: str, correo: str, programa_id: int) -> bool:
        sql = "UPDATE alumnos SET nombre=%s, correo=%s, programa_id=%s WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre, correo, programa_id, alumno_id))
                return cur.rowcount > 0

    @staticmethod
    def delete(alumno_id: int) -> bool:
        sql = "DELETE FROM alumnos WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (alumno_id,))
                return cur.rowcount > 0

    @staticmethod
    def promedio(alumno_id: int) -> Optional[float]:
        sql = "SELECT AVG(calificacion)::float FROM notas WHERE alumno_id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (alumno_id,))
                row = cur.fetchone()
                return float(row[0]) if row and row[0] is not None else None
