import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from app import handlers
from app.db import connect
from app.repository import TaskRepository
from app.services import TaskService

WEB = Path(__file__).parent / "web"
TYPES = {".html": "text/html", ".js": "text/javascript"}
service = TaskService(TaskRepository(connect("tasks.db")))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/tasks":
            return self._json(*handlers.list_tasks(service))
        name = "index.html" if self.path == "/" else self.path.lstrip("/")
        file = WEB / name
        if file.parent != WEB or not file.is_file():
            return self._json(404, {"error": "not found"})
        self.send_response(200)
        self.send_header("Content-Type", TYPES.get(file.suffix, "text/plain"))
        self.end_headers()
        self.wfile.write(file.read_bytes())

    def do_POST(self):
        if self.path != "/api/tasks":
            return self._json(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._json(400, {"error": "body must be JSON"})
        self._json(*handlers.create_task(service, body))

    def _json(self, status, payload):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
