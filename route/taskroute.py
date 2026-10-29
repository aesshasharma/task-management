
from fastapi import APIRouter, HTTPException
from model.taskmodel import Task
from controller import taskcontroller

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task):
    result = taskcontroller.create_task(task)

    if result is None:
        raise HTTPException(status_code=400, detail="Task ID already exists")

    return result

@router.get("/tasks")
def get_all_tasks():
    return taskcontroller.get_all_tasks()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    result = taskcontroller.get_task_by_id(task_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return result

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    result = taskcontroller.update_task(task_id, task)

    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return result

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    result = taskcontroller.delete_task(task_id)

    if not result:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
