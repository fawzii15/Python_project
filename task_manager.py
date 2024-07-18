import os
import json
from task import Task

class TaskManager:
    def __init__(self, file_path='tasks.txt'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(data) for data in tasks_data]
        return []
