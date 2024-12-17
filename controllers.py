# controllers.py

from models import System, Worker, Customer, Admin, Task

class SystemController:
    def __init__(self):
        self.system = System()

    def register_worker(self, username, password):
        worker = Worker(username, password)
        self.system.register_user(worker)

    def register_customer(self, username, password):
        customer = Customer(username, password)
        self.system.register_user(customer)

    def create_task(self, title, description):
        task = Task(title, description)
        self.system.create_task(task)

    def get_tasks(self):
        return self.system.get_tasks()