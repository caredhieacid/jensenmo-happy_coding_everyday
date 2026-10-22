import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db import connect
from app.handlers import list_tasks
from app.repository import TaskRepository
from app.services import TaskService


class ListTasksTests(unittest.TestCase):
    def setUp(self):
        self.conn = connect()
        self.conn.execute("INSERT INTO projects (id, name) VALUES (1, 'Billing')")
        self.conn.executemany(
            "INSERT INTO tasks (project_id, title, status) VALUES (?, ?, ?)",
            [(1, "Export CSV", "open"), (1, "Fix rounding", "done")],
        )
        self.service = TaskService(TaskRepository(self.conn))

    def test_lists_tasks_newest_first(self):
        status, body = list_tasks(self.service, "1")
        self.assertEqual(status, 200)
        self.assertEqual([task["title"] for task in body["tasks"]], ["Fix rounding", "Export CSV"])

    def test_unknown_project_is_404(self):
        self.assertEqual(list_tasks(self.service, "9")[0], 404)

    def test_non_integer_id_is_400(self):
        self.assertEqual(list_tasks(self.service, "abc")[0], 400)


if __name__ == "__main__":
    unittest.main()
