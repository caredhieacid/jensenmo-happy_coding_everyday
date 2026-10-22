class TaskRepository:
    def __init__(self, conn):
        self._conn = conn

    def project_exists(self, project_id):
        row = self._conn.execute("SELECT 1 FROM projects WHERE id = ?", (project_id,)).fetchone()
        return row is not None

    def list_tasks(self, project_id):
        rows = self._conn.execute(
            "SELECT id, title, status FROM tasks WHERE project_id = ? ORDER BY id DESC",
            (project_id,),
        ).fetchall()
        return [dict(row) for row in rows]
