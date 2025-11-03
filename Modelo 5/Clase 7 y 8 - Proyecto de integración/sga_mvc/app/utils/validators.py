import re
from .exceptions import DomainError


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(email: str) -> None:
    if not EMAIL_REGEX.match(email or ""):
        raise DomainError("Correo electrónico inválido.")


def validate_positive_int(value: int, field: str) -> None:
    if not isinstance(value, int) or value <= 0:
        raise DomainError(f"{field} debe ser un entero positivo.")


def validate_calificacion(value: float) -> None:
    try:
        f = float(value)
    except Exception as e:
        raise DomainError("Calificación debe ser numérica.") from e
    if f < 0 or f > 5:
        raise DomainError("Calificación debe estar entre 0 y 5.")
