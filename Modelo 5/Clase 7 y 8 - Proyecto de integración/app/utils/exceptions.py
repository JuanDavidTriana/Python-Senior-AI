class DomainError(Exception):
    """Base class for domain-specific errors."""

class NotFoundError(Exception):
    """Exception raised when a requested resource is not found."""

class IntegrityError(Exception):
    """Exception raised for integrity violations in the database."""