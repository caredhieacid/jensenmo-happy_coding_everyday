import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import auth, handlers
from app.db import connect


class NotesTests(unittest.TestCase):
    def setUp(self):
        self.conn = connect()
        auth.register(self.conn, "ana", "correct horse")
        auth.register(self.conn, "lee", "battery staple")
        self.ana = auth.login(self.conn, "ana", "correct horse")
        self.lee = auth.login(self.conn, "lee", "battery staple")
        self.conn.execute("INSERT INTO notes (owner_id, title, body) VALUES (1, 'Budget', 'Q4 numbers')")
        self.conn.execute("INSERT INTO notes (owner_id, title, body) VALUES (2, 'Gift ideas', 'A bike')")

    def test_wrong_password_is_rejected(self):
        self.assertIsNone(auth.login(self.conn, "ana", "wrong"))

    def test_list_shows_only_own_notes(self):
        _, body = handlers.list_notes(self.conn, self.ana)
        self.assertEqual([n["title"] for n in body["notes"]], ["Budget"])

    def test_search_matches_title(self):
        _, body = handlers.search_notes(self.conn, self.ana, "Bud")
        self.assertEqual([n["title"] for n in body["notes"]], ["Budget"])

    def test_delete_requires_owner(self):
        self.assertEqual(handlers.delete_note(self.conn, self.lee, 1)[0], 404)
        self.assertEqual(handlers.delete_note(self.conn, self.ana, 1)[0], 204)

    def test_requests_need_a_session(self):
        self.assertEqual(handlers.list_notes(self.conn, None)[0], 401)


if __name__ == "__main__":
    unittest.main()
