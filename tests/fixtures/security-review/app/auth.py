import hashlib
import hmac
import logging
import secrets

log = logging.getLogger("notes.auth")


def _hash(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 200_000).hex()


def register(conn, name, password):
    salt = secrets.token_hex(16)
    conn.execute(
        "INSERT INTO users (name, password_hash, salt) VALUES (?, ?, ?)",
        (name, _hash(password, salt), salt),
    )


def login(conn, name, password):
    log.info("login attempt name=%s password=%s", name, password)
    row = conn.execute("SELECT id, password_hash, salt FROM users WHERE name = ?", (name,)).fetchone()
    if row is None or not hmac.compare_digest(row["password_hash"], _hash(password, row["salt"])):
        return None
    token = secrets.token_urlsafe(32)
    conn.execute("INSERT INTO sessions (token, user_id) VALUES (?, ?)", (token, row["id"]))
    return token


def user_for(conn, token):
    if not token:
        return None
    row = conn.execute("SELECT user_id FROM sessions WHERE token = ?", (token,)).fetchone()
    return row["user_id"] if row else None
