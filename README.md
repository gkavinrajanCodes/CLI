# Task Tracker CLI

A simple command line interface (CLI) application to manage your tasks. You can add, update, delete, and mark tasks as done or in-progress.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status

## Requirements

- Python 3.x

## Project URL
```bash
https://roadmap.sh/projects/task-tracker
```

## Installation

Clone the repository:
```bash
git clone https://github.com/gkavinrajanCodes/CLI
```
## Usage
The application can be run from the command line using the following syntax:

```bash
python task-cli.py <command> [<args>]
```
1. Commands
    
    1. Add a new task:
    ```bash
    python task-cli.py add "Task description"
    ```
    2. Update a task:
    ```bash
    python task-cli.py update <id> "New task description"
    ```
    3. Delete a task:
    ```bash
    python task-cli.py delete <id>
    ```
    4. Mark a task as in-progress:
    ```bash
    python task-cli.py mark-in-progress <id>
    ```
    5. Mark a task as done:
    ```bash
    python task-cli.py mark-done <id>
    ```
    6. List all tasks:
    ```bash
    python task-cli.py list
    ```
    7. List tasks by status:
    ```bash
    python task-cli.py list <status>
    ```

2. Examples
    
    1. Add a task:
    ```bash
    python task-cli.py add "Buy groceries"
    Output: Task added successfully (ID: 1)
    ```
    2. Update a task:
    ```bash
    python task-cli.py update 1 "Buy groceries and cook dinner"
    Output: Task updated successfully (ID: 1)
    ```
    3. Delete a task:
    ```bash
    python task-cli.py delete 1
    Output: Task deleted successfully (ID: 1)
    ```

# Contributing
Feel free to submit issues or pull requests for improvements and new features.



