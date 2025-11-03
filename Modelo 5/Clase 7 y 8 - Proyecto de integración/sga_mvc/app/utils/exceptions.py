class DomainError(Exception):
    """Errores de validación de dominio o negocio."""


class NotFoundError(Exception):
    """Recurso solicitado no existe."""


class IntegrityError(Exception):
    """Violación de reglas de integridad de negocio."""
