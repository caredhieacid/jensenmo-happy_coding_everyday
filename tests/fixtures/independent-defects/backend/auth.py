SESSIONS = {"tok-ana": "ana", "tok-lee": "lee"}


def authenticate(headers):
    """Return (status, user). 401 when the bearer token is missing or unknown."""
    value = headers.get("Authorization", "")
    if not value.startswith("Bearer "):
        return 401, None
    user = SESSIONS.get(value[len("Bearer "):])
    return (200, user) if user else (401, None)
