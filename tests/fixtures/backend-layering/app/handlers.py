from app.services import ProjectNotFound


def list_tasks(service, project_id):
    try:
        tasks = service.list_tasks(int(project_id))
    except ValueError:
        return 400, {"error": "project id must be an integer"}
    except ProjectNotFound:
        return 404, {"error": "project not found"}
    return 200, {"tasks": tasks}


ROUTES = {
    ("GET", "/projects/{id}/tasks"): list_tasks,
}
