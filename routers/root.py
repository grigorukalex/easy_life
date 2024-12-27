from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from repository import TaskRepository
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router_pages = APIRouter(
    prefix="",
    tags=['Страницы']
)


@router_pages.get('/', summary='Главная страница')
def root():
    return {'data': 'Главная страница'}


@router_pages.get('/tasks', summary='Задачи', response_class=HTMLResponse)
async def tasks(request: Request):
    tasks_status_in_work = await TaskRepository.find_tasks_by_status(status=1)
    tasks_status_complete = await TaskRepository.find_tasks_by_status(status=2)
    tasks_status_postponed = await TaskRepository.find_tasks_by_status(status=3)
    tasks_status_garbage = await TaskRepository.find_tasks_by_status(status=4)
    print("tasks")
    return templates.TemplateResponse(
        request=request, name="tasks.html", context={
            "tasks": [{"status": "В работе",
                       "tasks": tasks_status_in_work},
                      {"status": "Завершённые",
                       "tasks": tasks_status_complete},
                      {"status": "Отложенные",
                       "tasks": tasks_status_postponed},
                      {"status": "Удалённые",
                       "tasks": tasks_status_garbage},
                      ]}
    )
