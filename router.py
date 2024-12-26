from fastapi import APIRouter, Depends
from typing import Annotated

from repository import TaskRepository
from schemas import NewTask, Task

router = APIRouter(
    prefix="/tasks",
tags=['Задачи']
)


@router.get('', summary='Получить все задачи')
async def get_tasks():
    tasks = await TaskRepository.find_all_tasks()
    return {"tasks": tasks}


@router.get('/{id_task}', summary='Получить конкретную задачу')
async def get_task(id_task: int):
    task = await TaskRepository.find_one_task(id_task)
    return {'data': task}
    # for task in tasks.tasks:
    #     if task.id == id_task:
    #         return {'data': task}
    # return HTTPException(status_code=404)


@router.post('', summary='Создать новую задачу')
async def create_task(
        new_task: Annotated[NewTask, Depends()]
):
    task: Task = Task(name=new_task.name, description=new_task.description)
    id_task = await TaskRepository.add_one_task(task)
    return {'success': 'ok', "id_task": id_task, 'description': 'Задача успешно добавлена'}


@router.post('/delete/{id_task}', summary='Удалить задачу')
async def delete_task(id_task: int):
    id_delete_task = await TaskRepository.delete_one_task(id_task)
    if id_delete_task == -1:
        return {'success': 'error_id', "id_task": id_task, 'description': 'Задача с таким номером не существует'}
    else:
        return {'success': 'ok', "id_task": id_delete_task, 'description': 'Задача успешно удалена'}