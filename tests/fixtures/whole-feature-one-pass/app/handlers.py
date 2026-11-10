from app.services import InvalidTask


def list_tasks(service):
    return 200, {"tasks": service.list()}


def create_task(service, body):
    try:
        task = service.create(body.get("title"))
    except InvalidTask as error:
        return 400, {"error": str(error)}
    return 201, task
