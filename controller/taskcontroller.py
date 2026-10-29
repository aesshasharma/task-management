
from model.taskmodel import Task

tasks = {}


def create_task(task: Task):
    if task.id in tasks:
        return None

    tasks[task.id] = task
    return task

def get_all_tasks():
    return list(tasks.values())

def get_task_by_id(task_id: int):
    return tasks.get(task_id)

def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        return None

    tasks[task_id] = task
    return task

def delete_task(task_id: int):
    if task_id not in tasks:
        return False

    tasks.pop(task_id)
    return True
