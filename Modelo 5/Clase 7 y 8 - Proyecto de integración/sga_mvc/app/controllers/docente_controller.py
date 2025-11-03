from typing import List, Optional

from app.models.docente import Docente
from app.repositories.docente_repo import DocenteRepository
from app.utils.validators import validate_email
from app.utils.exceptions import DomainError, IntegrityError, NotFoundError


class DocenteController:
    @staticmethod
    def crear(nombre: str, correo: str) -> Docente:
        validate_email(correo)
        # Validar unicidad manual para mejor mensaje
        existente = DocenteRepository.get_by_email(correo)
        if existente:
            raise DomainError("El correo de docente ya está registrado.")
        return DocenteRepository.create(nombre, correo)

    @staticmethod
    def listar() -> List[Docente]:
        return DocenteRepository.get_all()

    @staticmethod
    def obtener(docente_id: int) -> Docente:
        d = DocenteRepository.get_by_id(docente_id)
        if not d:
            raise NotFoundError("Docente no encontrado.")
        return d

    @staticmethod
    def actualizar(docente_id: int, nombre: str, correo: str) -> None:
        validate_email(correo)
        # Verificar que existe
        DocenteController.obtener(docente_id)
        # Unicidad: si hay otro con mismo correo, error
        otro = DocenteRepository.get_by_email(correo)
        if otro and otro.id != docente_id:
            raise DomainError("El correo de docente ya está registrado por otro docente.")
        ok = DocenteRepository.update(docente_id, nombre, correo)
        if not ok:
            raise NotFoundError("No se pudo actualizar el docente.")

    @staticmethod
    def eliminar(docente_id: int) -> None:
        # Regla: no se puede eliminar si tiene programas
        programas = DocenteRepository.count_programas(docente_id)
        if programas > 0:
            raise IntegrityError("No se puede eliminar el docente: tiene programas asociados.")
        ok = DocenteRepository.delete(docente_id)
        if not ok:
            raise NotFoundError("Docente no encontrado para eliminar.")
