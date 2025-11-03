from typing import List

from app.models.programa import Programa
from app.repositories.programa_repo import ProgramaRepository
from app.controllers.docente_controller import DocenteController
from app.utils.validators import validate_positive_int
from app.utils.exceptions import NotFoundError


class ProgramaController:
    @staticmethod
    def crear(nombre: str, duracion: int, docente_id: int | None) -> Programa:
        validate_positive_int(duracion, "Duración")
        # Si se pasa docente_id, validar que exista
        if docente_id is not None:
            DocenteController.obtener(docente_id)
        return ProgramaRepository.create(nombre, duracion, docente_id)

    @staticmethod
    def listar() -> List[Programa]:
        return ProgramaRepository.get_all()

    @staticmethod
    def obtener(programa_id: int) -> Programa:
        p = ProgramaRepository.get_by_id(programa_id)
        if not p:
            raise NotFoundError("Programa no encontrado.")
        return p

    @staticmethod
    def actualizar(programa_id: int, nombre: str, duracion: int, docente_id: int | None) -> None:
        validate_positive_int(duracion, "Duración")
        ProgramaController.obtener(programa_id)
        if docente_id is not None:
            DocenteController.obtener(docente_id)
        ok = ProgramaRepository.update(programa_id, nombre, duracion, docente_id)
        if not ok:
            raise NotFoundError("No se pudo actualizar el programa.")

    @staticmethod
    def eliminar(programa_id: int) -> None:
        ok = ProgramaRepository.delete(programa_id)
        if not ok:
            raise NotFoundError("Programa no encontrado para eliminar.")
