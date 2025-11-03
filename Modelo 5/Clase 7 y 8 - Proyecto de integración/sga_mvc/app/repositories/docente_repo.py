from typing import List, Optional
import psycopg2

from app.db.connection import get_connection
from app.models.docente import Docente


class DocenteRepository:
    @staticmethod
    def create(nombre: str, correo: str) -> Docente:
        sql = "INSERT INTO docentes(nombre, correo) VALUES (%s, %s) RETURNING id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(sql, (nombre, correo))
                    new_id = cur.fetchone()[0]
                    return Docente(id=new_id, nombre=nombre, correo=correo)
                except psycopg2.Error as e:
                    raise

    @staticmethod
    def get_by_id(docente_id: int) -> Optional[Docente]:
        sql = "SELECT id, nombre, correo FROM docentes WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (docente_id,))
                row = cur.fetchone()
                if not row:
                    return None
                return Docente(id=row[0], nombre=row[1], correo=row[2])

    @staticmethod
    def get_by_email(correo: str) -> Optional[Docente]:
        sql = "SELECT id, nombre, correo FROM docentes WHERE correo = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (correo,))
                row = cur.fetchone()
                if not row:
                    return None
                return Docente(id=row[0], nombre=row[1], correo=row[2])

    @staticmethod
    def get_all() -> List[Docente]:
        sql = "SELECT id, nombre, correo FROM docentes ORDER BY id"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                return [Docente(id=r[0], nombre=r[1], correo=r[2]) for r in rows]

    @staticmethod
    def update(docente_id: int, nombre: str, correo: str) -> bool:
        sql = "UPDATE docentes SET nombre=%s, correo=%s WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(sql, (nombre, correo, docente_id))
                    return cur.rowcount > 0
                except psycopg2.Error:
                    raise

    @staticmethod
    def delete(docente_id: int) -> bool:
        sql = "DELETE FROM docentes WHERE id=%s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (docente_id,))
                return cur.rowcount > 0

    @staticmethod
    def count_programas(docente_id: int) -> int:
        sql = "SELECT COUNT(*) FROM programas WHERE docente_id = %s"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (docente_id,))
                return int(cur.fetchone()[0])
