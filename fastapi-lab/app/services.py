from .repositories import ITaskRepository
from .models import Task, TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Business logic could go here
        return self.repo.create(task_in)
    
    def mark_as_complete(self, task_id: int) -> Task | None:
     task = self.repository.get_by_id(task_id)
     if task:
        task.is_completed = True 
        return self.repository.update(task_id, task)
     return None