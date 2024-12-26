from fastapi import APIRouter

router_pages = APIRouter(
    prefix="",
    tags=['Страницы']
)


@router_pages.get('/', summary='Главная страница')
def root():
    return {'data': 'Главная страница'}

@router_pages.get('/tasks', summary='Задачи')
def tasks():
    return {'data': 'Задачи'}
