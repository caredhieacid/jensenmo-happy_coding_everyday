"""Signup handling for the demo service."""

_USERS: dict[str, dict] = {}


def register(username: str, email: str, password: str) -> dict:
    """Create an account and return the stored record."""
    record = {"username": username, "email": email, "password": password}
    _USERS[username] = record
    return record


def reset() -> None:
    _USERS.clear()
