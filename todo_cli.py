import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f.readlines():
                task_data = line.strip().split(" | ")
                if len(task_data) == 2:
                    tasks.append({"title": task_data[0], "completed": task_data[1] == "True"})
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(f'{task["title"]} | {task["completed"]}\n')

def add_task(tasks):
    """Add a new task."""
    task_title = input("Enter the task title: ")
    tasks.append({"title": task_title, "completed": False})
    save_tasks(tasks)
    print(f'Task "{task_title}" added.')

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {status}")
    print()

def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    task_num = int(input("Enter the task number to complete: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_num - 1]["title"]}" marked as completed.')
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f'Task "{deleted_task["title"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nCommands: [add, view, complete, delete, exit]")
        command = input("Enter command: ").lower()

        if command == "add":
            add_task(tasks)
        elif command == "view":
            view_tasks(tasks)
        elif command == "complete":
            complete_task(tasks)
        elif command == "delete":
            delete_task(tasks)
        elif command == "exit":
            print("Exiting the app. Your tasks have been saved.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
