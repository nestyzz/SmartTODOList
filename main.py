from typing import Union

import requests
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    id: int
    name: str = "Новая задача"
    description: str = "Описание задачи"
    is_done: bool = False


@app.post("/tasks/")
def create_task(name: str, description: str):
    id_task = len(tasks) + 1
    new_task = Task(id=id_task, name=name, description=description, is_done=False)
    tasks.append(new_task)
    return new_task


@app.get("/tasks/")
def get_tasks():
    return tasks
