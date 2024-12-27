import json
import csv
from abc import ABC, abstractmethod
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'No Due Date'}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

class StorageHandler(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorageHandler(StorageHandler):
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self):
        try:
            with open(self.filename, "r") as file:
                return [Task.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

class CSVStorageHandler(StorageHandler):
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            writer.writerows(task.to_dict() for task in tasks)

    def load(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []

class ToDoApp:
    def __init__(self, storage_handler):
        self.tasks = []
        self.storage_handler = storage_handler
        self.tasks = self.storage_handler.load()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Task ID must be unique.")
            return
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = kwargs.get("title", task.title)
                task.description = kwargs.get("description", task.description)
                task.due_date = kwargs.get("due_date", task.due_date)
                task.status = kwargs.get("status", task.status)
                print("Task updated successfully!")
                return
        print("Task ID not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the given status.")
            return
        print("Filtered Tasks:")
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.storage_handler.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage_handler.load()
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
            """)
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                task_id = input("Enter Task ID: ").strip()
                title = input("Enter Title: ").strip()
                description = input("Enter Description: ").strip()
                due_date = input("Enter Due Date (YYYY-MM-DD, press Enter to skip): ").strip()
                status = input("Enter Status (Pending/In Progress/Completed): ").strip()
                self.add_task(Task(task_id, title, description, due_date or None, status))

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                task_id = input("Enter Task ID to update: ").strip()
                title = input("Enter new Title (press Enter to skip): ").strip() or None
                description = input("Enter new Description (press Enter to skip): ").strip() or None
                due_date = input("Enter new Due Date (YYYY-MM-DD, press Enter to skip): ").strip() or None
                status = input("Enter new Status (press Enter to skip): ").strip() or None
                self.update_task(task_id, title=title, description=description, due_date=due_date, status=status)

            elif choice == "4":
                task_id = input("Enter Task ID to delete: ").strip()
                self.delete_task(task_id)

            elif choice == "5":
                status = input("Enter status to filter by (Pending/In Progress/Completed): ").strip()
                self.filter_tasks(status)

            elif choice == "6":
                self.save_tasks()

            elif choice == "7":
                self.load_tasks()

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    storage_choice = input("Choose storage format (1: JSON, 2: CSV): ").strip()
    if storage_choice == "1":
        storage = JSONStorageHandler("tasks.json")
    elif storage_choice == "2":
        storage = CSVStorageHandler("tasks.csv")
    else:
        print("Invalid choice, defaulting to JSON.")
        storage = JSONStorageHandler("tasks.json")

    app = ToDoApp(storage)
    app.menu()
