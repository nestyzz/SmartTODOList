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


@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в SmartToDoList!"}


@app.post("/tasks/")
def create_task(name: str, description: str):
    id_task = len(tasks) + 1
    new_task = Task(id=id_task, name=name, description=description, is_done=False)
    tasks.append(new_task)
    return new_task


@app.put("/tasks/")
def update_task(id: int, name: str = None, description: str = None, is_done: bool = None):
    for item in tasks:
        if item.id == id:
            index = tasks.index(item)
            old_task = item.copy()
            updated_task = Task(id=id,
                                name=name if name is not None else old_task.name,
                                description=description if description is not None else old_task.description,
                                is_done=is_done if is_done is not None else old_task.is_done)
            tasks.pop(index)
            tasks.append(updated_task)
            tasks.sort(key=lambda t: int(t.id))


@app.get("/tasks/")
def get_tasks():
    return tasks

# Для запуска использовать команду
# uvicorn main:app --reload
