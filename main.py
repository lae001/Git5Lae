# main.py

import tkinter as tk
from tkinter import messagebox
from controllers import SystemController

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Система управления наемной работой")
        self.controller = SystemController()

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Регистрация пользователя
        tk.Label(self.root, text="Регистрация пользователя").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Имя пользователя:").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Пароль:").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Зарегистрировать рабочего", command=self.register_worker).grid(row=3, column=0, pady=10)
        tk.Button(self.root, text="Зарегистрировать заказчика", command=self.register_customer).grid(row=3, column=1, pady=10)

        # Создание задания
        tk.Label(self.root, text="Создание задания").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Название задания:").grid(row=5, column=0)
        self.task_title_entry = tk.Entry(self.root)
        self.task_title_entry.grid(row=5, column=1)

        tk.Label(self.root, text="Описание задания:").grid(row=6, column=0)
        self.task_description_entry = tk.Entry(self.root)
        self.task_description_entry.grid(row=6, column=1)

        tk.Button(self.root, text="Создать задание", command=self.create_task).grid(row=7, column=0, columnspan=2, pady=10)

        # Просмотр заданий
        tk.Button(self.root, text="Просмотреть задания", command=self.view_tasks).grid(row=8, column=0, columnspan=2, pady=10)

    def register_worker(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.register_worker(username, password)
        messagebox.showinfo("Успех", f"Рабочий {username} зарегистрирован")

    def register_customer(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.register_customer(username, password)
        messagebox.showinfo("Успех", f"Заказчик {username} зарегистрирован")

    def create_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get()
        self.controller.create_task(title, description)
        messagebox.showinfo("Успех", f"Задание '{title}' создано")

    def view_tasks(self):
        tasks = self.controller.get_tasks()
        tasks_text = "\n".join([f"{task.title}: {task.description}" for task in tasks])
        messagebox.showinfo("Задания", tasks_text if tasks_text else "Нет доступных заданий")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()