from sqlalchemy import select

from database import new_session, TasksOrm
from schemas import Task


class TaskRepository:
    @classmethod
    async def add_one_task(cls, data: Task):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id_task

    @classmethod
    async def find_all_tasks(cls):
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return  task_models

    @classmethod
    async def find_one_task(cls, id_task: int):
        async with new_session() as session:
            query = select(TasksOrm).filter_by(id_task=id_task)
            print(query)
            result = await session.execute(query)
            print(result)
            task = result.scalar_one_or_none()
            return  task