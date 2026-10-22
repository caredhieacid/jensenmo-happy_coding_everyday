class ProjectNotFound(Exception):
    pass


class TaskService:
    def __init__(self, repository):
        self._repository = repository

    def list_tasks(self, project_id):
        if not self._repository.project_exists(project_id):
            raise ProjectNotFound(project_id)
        return self._repository.list_tasks(project_id)
