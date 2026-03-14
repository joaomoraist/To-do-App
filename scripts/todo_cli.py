import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else " "
        print(f"{i+1}. [{status}] {t['task']}")

def complete_task(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed!")

while True:
    print("\n1 - Add task")
    print("2 - List tasks")
    print("3 - Complete task")
    print("4 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        add_task(task)

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        idx = int(input("Task number: ")) - 1
        complete_task(idx)

    elif choice == "4":
        break