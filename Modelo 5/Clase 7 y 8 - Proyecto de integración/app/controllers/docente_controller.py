from typing import List

from app.models.docente import Docente
from app.repository.docente_repo import DocenteRepository
from app.utils.validators import validate_email
from app.utils.exceptions import DomainError, IntegrityError, NotFoundError

class DocentreController:
    """Controlador para operaciones de docentes.

    Encapsula la lógica de negocio para crear, listar, obtener, actualizar y eliminar docentes.
    """

    @staticmethod
    def crear(nombre:str, correo:str) -> Docente:
        """Crea un nuevo docente.

        Args:
            nombre (str): Nombre completo del docente.
            correo (str): Correo electrónico del docente.

        Raises:
            DomainError: Si el correo es inválido o ya está registrado por otro docente.
        """
        validate_email(correo)
        existente = DocenteRepository.get_by_email(correo)
        if existente:
            raise DomainError("El correo de docente ya esta registrado")
        return DocenteRepository.create(nombre,correo)

    @staticmethod
    def listar() -> List[Docente]:
        """Lista todos los docentes registrados.

        Returns:
            List[Docente]: Lista de docentes.
        """
        return DocenteRepository.get_all()
    
    @staticmethod
    def obtener(docente_id: int) -> Docente:
        """Obtiene un docente por su identificador.

        Args:
            docente_id (int): Identificador del docente.

        Raises:
            NotFoundError: Si no existe un docente con el ID proporcionado.
        """
        d = DocenteRepository.get_by_id(docente_id)
        if not d:
            raise NotFoundError("Docente no encontrado.")
        return d
    
    @staticmethod
    def actualizar(docente_id: int, nombre:str, correo:str) -> None:
        """Actualiza los datos de un docente.

        Args:
            docente_id (int): Identificador del docente a actualizar.
            nombre (str): Nuevo nombre del docente.
            correo (str): Nuevo correo electrónico del docente.

        Raises:
            DomainError: Si el correo es inválido o ya pertenece a otro docente.
            NotFoundError: Si el docente a actualizar no existe.
        """
        validate_email(correo)
        otro = DocenteRepository.get_by_email(correo)
        if otro and otro.id != docente_id:
            raise DomainError("El correo de docente ya esta registrado por otro docente")
        actualizado = DocenteRepository.update(docente_id,nombre,correo)
        if not actualizado:
            raise NotFoundError("No se pudo actulizar el docente")
        
    @staticmethod
    def eliminar(docente_id:int) ->None:
        """Elimina un docente por su identificador.

        Args:
            docente_id (int): Identificador del docente a eliminar.

        Raises:
            IntegrityError: Si el docente tiene programas asociados y no puede eliminarse.
            NotFoundError: Si el docente no existe.
        """
        programas_docente = DocenteRepository.count_programas(docente_id)
        if programas_docente > 0:
            raise IntegrityError("No se puede eliminar el docente: tiene programas asociados")
        elimando = DocenteRepository.delete(docente_id)
        if not elimando:
            raise NotFoundError("Docene no encontrado para la eliminar")
        
    
