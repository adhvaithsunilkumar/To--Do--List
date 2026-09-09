import tkinter as tk
from tkinter import messagebox


# Task class
class Task:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_completed(self):
        self.completed = True


# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(Task(task))

    def complete_task(self, number):
        self.tasks[number].mark_completed()

    def delete_task(self, number):
        self.tasks.pop(number)


# GUI Controller
class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()

        root.title("Adhvaith Sunilkumar - To-Do List")
        root.geometry("500x500")

        # Title
        title = tk.Label(
            root,
            text="TO-DO LIST",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        # Task input
        self.task_entry = tk.Entry(
            root,
            font=("Arial", 14),
            width=30
        )
        self.task_entry.pack(pady=10)

        # Add button
        add_button = tk.Button(
            root,
            text="Add Task",
            width=20,
            command=self.add_task
        )
        add_button.pack(pady=5)

        # Task list
        self.task_list = tk.Listbox(
            root,
            font=("Arial", 13),
            width=45,
            height=12
        )
        self.task_list.pack(pady=15)

        # Complete button
        complete_button = tk.Button(
            root,
            text="Mark as Completed",
            width=20,
            command=self.complete_task
        )
        complete_button.pack(pady=5)

        # Delete button
        delete_button = tk.Button(
            root,
            text="Delete Task",
            width=20,
            command=self.delete_task
        )
        delete_button.pack(pady=5)

    # Add task
    def add_task(self):
        task = self.task_entry.get()

        if task == "":
            messagebox.showwarning("Warning", "Please enter a task")
            return

        self.manager.add_task(task)
        self.task_entry.delete(0, tk.END)

        self.display_tasks()

    # Display tasks
    def display_tasks(self):
        self.task_list.delete(0, tk.END)

        for task in self.manager.tasks:
            if task.completed:
                self.task_list.insert(
                    tk.END,
                    "✓ " + task.task + " - Completed"
                )
            else:
                self.task_list.insert(
                    tk.END,
                    "○ " + task.task + " - Pending"
                )

    # Complete task
    def complete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a task"
            )
            return

        number = selected[0]

        self.manager.complete_task(number)

        self.display_tasks()

    # Delete task
    def delete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a task"
            )
            return

        number = selected[0]

        self.manager.delete_task(number)

        self.display_tasks()


# Controller
root = tk.Tk()

app = TaskApp(root)

root.mainloop()
