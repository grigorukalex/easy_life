import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from database import create_tables
from routers.tasks import router_tasks
from routers.root import router_pages


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)
app.include_router(router_tasks)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

# class Tasks(BaseModel):
#     num_id: int = Field(default=0)
#     tasks: list[Task] = []
#
#     def add_new_task(self, new_task: NewTask):
#         task: Task = Task(name=new_task.name, description=new_task.description)
#         self.num_id += 1
#         task.id = self.num_id
#         self.tasks.append(task)


# tasks: Tasks = Tasks()
# tasks.add_new_task(NewTask(name='Сделать авторизацию'))
# tasks.add_new_task(NewTask(name='Прикрутить базу данных'))
# tasks.add_new_task(NewTask(name='Сделать вебстраницу с задачами'))
# tasks.add_new_task(NewTask(name='Сделать меню навигации по страницам'))
