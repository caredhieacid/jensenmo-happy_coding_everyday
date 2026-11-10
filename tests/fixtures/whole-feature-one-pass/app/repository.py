class TaskRepository:
    def __init__(self, conn):
        self._conn = conn

    def add(self, title):
        cursor = self._conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        self._conn.commit()
        return self.get(cursor.lastrowid)

    def get(self, task_id):
        row = self._conn.execute(
            "SELECT id, title, done FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        return _to_task(row)

    def list(self):
        rows = self._conn.execute("SELECT id, title, done FROM tasks ORDER BY id DESC").fetchall()
        return [_to_task(row) for row in rows]


def _to_task(row):
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}
