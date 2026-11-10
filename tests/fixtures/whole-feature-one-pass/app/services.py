class InvalidTask(Exception):
    pass


class TaskService:
    def __init__(self, repository):
        self._repository = repository

    def create(self, title):
        title = (title or "").strip()
        if not title:
            raise InvalidTask("title is required")
        return self._repository.add(title)

    def list(self):
        return self._repository.list()
