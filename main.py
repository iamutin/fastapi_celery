from typing import Any

from celery.result import AsyncResult
from fastapi import FastAPI

from app.tasks import background_task

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to FastAPI with Celery"}


@app.post("/task")
async def run_task() -> dict[str, str]:
    task = background_task.delay()
    return {"task_id": task.id}


@app.get("/task/{task_id}")
async def get_result(task_id: str) -> dict[str, Any]:
    task = AsyncResult(task_id, app=background_task.app)
    if task.ready():
        return {
            "task_id": task_id,
            "status": task.status,
            "result": task.result,
            "ready": True,
        }
    return {
        "task_id": task_id,
        "status": task.status,
        "result": None,
        "ready": False,
    }
