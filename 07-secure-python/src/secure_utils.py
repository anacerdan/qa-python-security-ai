from hashlib import sha256
import secrets


def generate_token(nbytes: int = 32) -> str:
    """Generate a cryptographically secure random token."""
    if nbytes < 16:
        raise ValueError("Token size is too small")
    return secrets.token_urlsafe(nbytes)


def checksum(value: str) -> str:
    """Create a non-secret integrity checksum."""
    return sha256(value.encode("utf-8")).hexdigest()
