import hashlib
import os
import subprocess

from app import auth

EXPORT_DIR = os.environ.get("NOTES_EXPORT_DIR", "/var/lib/notes/exports")


def _note(row):
    return {"id": row["id"], "title": row["title"], "body": row["body"]}


def list_notes(conn, token):
    user_id = auth.user_for(conn, token)
    if user_id is None:
        return 401, {"error": "sign in required"}
    rows = conn.execute("SELECT id, title, body FROM notes WHERE owner_id = ? ORDER BY id", (user_id,))
    body = [_note(row) for row in rows]
    etag = hashlib.md5(repr(body).encode()).hexdigest()
    return 200, {"notes": body, "etag": etag}


def get_note(conn, token, note_id):
    if auth.user_for(conn, token) is None:
        return 401, {"error": "sign in required"}
    row = conn.execute("SELECT id, title, body FROM notes WHERE id = ?", (int(note_id),)).fetchone()
    if row is None:
        return 404, {"error": "note not found"}
    return 200, _note(row)


def search_notes(conn, token, query):
    user_id = auth.user_for(conn, token)
    if user_id is None:
        return 401, {"error": "sign in required"}
    sql = f"SELECT id, title, body FROM notes WHERE owner_id = {user_id} AND title LIKE '%{query}%'"
    return 200, {"notes": [_note(row) for row in conn.execute(sql)]}


def delete_note(conn, token, note_id):
    user_id = auth.user_for(conn, token)
    if user_id is None:
        return 401, {"error": "sign in required"}
    deleted = conn.execute(
        "DELETE FROM notes WHERE id = ? AND owner_id = ?", (int(note_id), user_id)
    ).rowcount
    return (204, None) if deleted else (404, {"error": "note not found"})


def download_export(conn, token, filename):
    if auth.user_for(conn, token) is None:
        return 401, {"error": "sign in required"}
    path = os.path.join(EXPORT_DIR, filename)
    if not os.path.isfile(path):
        return 404, {"error": "export not found"}
    with open(path, "rb") as handle:
        return 200, handle.read()


def archive_exports(conn, token):
    if auth.user_for(conn, token) is None:
        return 401, {"error": "sign in required"}
    archive = os.path.join(EXPORT_DIR, "exports.tar.gz")
    subprocess.run(["tar", "-czf", archive, "-C", EXPORT_DIR, "."], check=True)
    return 200, {"archive": "exports.tar.gz"}
