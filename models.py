# models.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Worker(User):
    def apply_for_task(self, task):
        print(f"Worker {self.username} applied for task: {task.title}")

class Customer(User):
    def create_task(self, task):
        print(f"Customer {self.username} created task: {task.title}")

class Admin(User):
    def manage_users(self):
        print(f"Admin {self.username} is managing users")

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Open"

class System:
    def __init__(self):
        self.users = []
        self.tasks = []

    def register_user(self, user):
        self.users.append(user)
        print(f"User {user.username} registered")

    def create_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' created")

    def get_tasks(self):
        return self.tasks