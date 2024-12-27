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
    tasks = await TaskRepository.find_all_tasks()
    print(tasks)
    return templates.TemplateResponse(
        request=request, name="tasks.html", context={"tasks": tasks}
    )
