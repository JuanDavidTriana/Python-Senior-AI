from typing import List, Optional

from app.models.alumno import Alumno
from app.repositories.alumno_repo import AlumnoRepository
from app.controllers.programa_controller import ProgramaController
from app.utils.validators import validate_email
from app.utils.exceptions import DomainError, NotFoundError


class AlumnoController:
    @staticmethod
    def crear(nombre: str, correo: str, programa_id: int) -> Alumno:
        validate_email(correo)
        ProgramaController.obtener(programa_id)
        # Unicidad correo
        existente = AlumnoRepository.get_by_email(correo)
        if existente:
            raise DomainError("El correo del alumno ya está registrado.")
        return AlumnoRepository.create(nombre, correo, programa_id)

    @staticmethod
    def listar() -> List[Alumno]:
        return AlumnoRepository.get_all()

    @staticmethod
    def obtener(alumno_id: int) -> Alumno:
        a = AlumnoRepository.get_by_id(alumno_id)
        if not a:
            raise NotFoundError("Alumno no encontrado.")
        return a

    @staticmethod
    def actualizar(alumno_id: int, nombre: str, correo: str, programa_id: int) -> None:
        validate_email(correo)
        AlumnoController.obtener(alumno_id)
        ProgramaController.obtener(programa_id)
        otro = AlumnoRepository.get_by_email(correo)
        if otro and otro.id != alumno_id:
            raise DomainError("El correo del alumno ya está registrado por otro alumno.")
        ok = AlumnoRepository.update(alumno_id, nombre, correo, programa_id)
        if not ok:
            raise NotFoundError("No se pudo actualizar el alumno.")

    @staticmethod
    def eliminar(alumno_id: int) -> None:
        ok = AlumnoRepository.delete(alumno_id)
        if not ok:
            raise NotFoundError("Alumno no encontrado para eliminar.")

    @staticmethod
    def promedio(alumno_id: int) -> Optional[float]:
        AlumnoController.obtener(alumno_id)
        return AlumnoRepository.promedio(alumno_id)
