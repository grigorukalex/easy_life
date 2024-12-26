from pydantic import BaseModel, Field
from enum import Enum

# Статусы задач
class TaskStatus(Enum):
    IN_WORK = 1  # В РАБОТЕ
    COMPLETE = 2  # ЗАВЕРШЕНА
    POSTPONED = 3  # ОТЛОЖЕНА
    GARBAGE = 4  # В КОРЗИНЕ


class NewTask(BaseModel):
    name: str = Field(max_length=255)
    description: str | None = Field(max_length=10000, default=None)


class Task(NewTask):
    id_task: int = Field(default=None, alias="id_task")
    # status: int = 1
    status: int = Field(default=1)
    # status: int = Field(default=TaskStatus.IN_WORK)
    # status: TaskStatus = Field(default=TaskStatus.IN_WORK)


