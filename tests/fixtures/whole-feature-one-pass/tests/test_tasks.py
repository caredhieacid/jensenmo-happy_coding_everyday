import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import handlers
from app.db import connect
from app.repository import TaskRepository
from app.services import TaskService


class TaskTests(unittest.TestCase):
    def setUp(self):
        self.service = TaskService(TaskRepository(connect()))

    def test_create_and_list_newest_first(self):
        handlers.create_task(self.service, {"title": "Write report"})
        status, task = handlers.create_task(self.service, {"title": "Book room"})
        self.assertEqual(status, 201)
        self.assertEqual(task["title"], "Book room")
        _, body = handlers.list_tasks(self.service)
        self.assertEqual([t["title"] for t in body["tasks"]], ["Book room", "Write report"])

    def test_blank_title_is_rejected(self):
        status, body = handlers.create_task(self.service, {"title": "  "})
        self.assertEqual(status, 400)
        self.assertEqual(body, {"error": "title is required"})


if __name__ == "__main__":
    unittest.main()
