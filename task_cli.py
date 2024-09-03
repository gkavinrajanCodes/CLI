import sys
import json
from datetime import datetime
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update an existing task's description
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")

# Mark a task as in-progress or done
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

# List all tasks
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']}, Updated: {task['updatedAt']})")

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: task-cli <command> [<args>]")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Usage: task-cli add <description>")
            return
        add_task(args[1])

    elif command == "update":
        if len(args) < 3:
            print("Usage: task-cli update <id> <new_description>")
            return
        try:
            task_id = int(args[1])
            update_task(task_id, args[2])
        except ValueError:
            print("Invalid ID. Please provide a valid numeric ID.")

    elif command == "delete":
        if len(args) < 2:
            print("Usage: task-cli delete <id>")
            return
        try:
            task_id = int(args[1])
            delete_task(task_id)
        except ValueError:
            print("Invalid ID. Please provide a valid numeric ID.")

    elif command == "mark-in-progress":
        if len(args) < 2:
            print("Usage: task-cli mark-in-progress <id>")
            return
        try:
            task_id = int(args[1])
            mark_task(task_id, "in-progress")
        except ValueError:
            print("Invalid ID. Please provide a valid numeric ID.")

    elif command == "mark-done":
        if len(args) < 2:
            print("Usage: task-cli mark-done <id>")
            return
        try:
            task_id = int(args[1])
            mark_task(task_id, "done")
        except ValueError:
            print("Invalid ID. Please provide a valid numeric ID.")

    elif command == "list":
        if len(args) == 1:
            list_tasks()
        elif args[1] in ["done", "todo", "in-progress"]:
            list_tasks(args[1])
        else:
            print("Usage: task-cli list [done|todo|in-progress]")

    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == "__main__":
    main()
