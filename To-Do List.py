class Task:
    def To_DoList(self, description):
        self.description = description
        self.completed = False

    def complete_task(self):
        self.completed = True

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.description}"

class To_Do_List:
    def To_DoList(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete_task()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

def Work():
    todo_list = To_Do_List()
    while True:
        print("\nTo-Do List:")
        todo_list.display_tasks()
        print("\nOptions: add [task], complete [index], delete [index], exit")
        command = input("Enter command: ").split()
        action = command[0]
        if action == "add":
            todo_list.add_task(' '.join(command[1:]))
        elif action == "complete" and len(command) == 2 and command[1].isdigit():
            todo_list.complete_task(int(command[1]))
        elif action == "delete" and len(command) == 2 and command[1].isdigit():
            todo_list.delete_task(int(command[1]))
        elif action == "exit":
            break
        else:
            print("Invalid command. Please try again.")



    Work()

