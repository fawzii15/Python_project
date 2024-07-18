import datetime

class Task:
    def __init__(self, title, description='', due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else datetime.datetime.now()
        self.completed = False

    def __str__(self):
        return f"Task(title={self.title}, description={self.description}, due_date={self.due_date}, completed={self.completed})"

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S'),
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        due_date = datetime.datetime.strptime(data['due_date'], '%Y-%m-%d %H:%M:%S')
        task = Task(data['title'], data['description'], due_date)
        if data['completed']:
            task.complete()
        return task
