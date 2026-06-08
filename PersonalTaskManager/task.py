class Task:
    def __init__(self,task_id,title,description,priority,completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed

    