from typing import List

from app.models.nota import Nota
from app.repositories.nota_repo import NotaRepository
from app.controllers.alumno_controller import AlumnoController
from app.utils.validators import validate_calificacion
from app.utils.exceptions import NotFoundError


class NotaController:
    @staticmethod
    def crear(alumno_id: int, asignatura: str, calificacion: float) -> Nota:
        AlumnoController.obtener(alumno_id)
        validate_calificacion(calificacion)
        return NotaRepository.create(alumno_id, asignatura, float(calificacion))

    @staticmethod
    def listar_por_alumno(alumno_id: int) -> List[Nota]:
        AlumnoController.obtener(alumno_id)
        return NotaRepository.get_all_by_alumno(alumno_id)

    @staticmethod
    def obtener(nota_id: int) -> Nota:
        n = NotaRepository.get_by_id(nota_id)
        if not n:
            raise NotFoundError("Nota no encontrada.")
        return n

    @staticmethod
    def actualizar(nota_id: int, asignatura: str, calificacion: float) -> None:
        validate_calificacion(calificacion)
        NotaController.obtener(nota_id)
        ok = NotaRepository.update(nota_id, asignatura, float(calificacion))
        if not ok:
            raise NotFoundError("No se pudo actualizar la nota.")

    @staticmethod
    def eliminar(nota_id: int) -> None:
        ok = NotaRepository.delete(nota_id)
        if not ok:
            raise NotFoundError("Nota no encontrada para eliminar.")
