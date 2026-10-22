import sqlite3

SCHEMA = """
CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    project_id INTEGER NOT NULL REFERENCES projects(id),
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('open', 'done'))
);
"""


def connect():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn
