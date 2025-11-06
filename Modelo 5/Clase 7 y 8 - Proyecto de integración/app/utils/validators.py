import re
from .exceptions import DomainError


EMAIL_REGEX = re.compile(f"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate_email(email: str) -> None:
    if not EMAIL_REGEX.match(email or ""):
        raise DomainError("Corroe Electronico inválido.")
    
    