# --- Import Required Modules ---
import json
import os

# --- ANSI Color Codes for Displaying Priorities ---
COLOR_RESET = '\033[0m'
COLOR_RED = '\033[91m'
COLOR_YELLOW = '\033[93m'
COLOR_GREEN = '\033[92m'

# --- Command Dictionary ---
todo_commands = {
    "add": {"keywords": ["add", "new", "create"], "description": "Add a new task to the list"},
    "remove": {"keywords": ["remove", "delete", "rm"], "description": "Delete a task from the list"},
    "list": {"keywords": ["list", "show list", "ls", "sl", "l"], "description": "Show the full list of tasks"},
    "edit": {"keywords": ["edit", "update", "change"], "description": "Edit an existing task"},
    "save": {"keywords": ["save", "write"], "description": "Save the current list to file"},
    "done": {"keywords": ["done", "exit", "quit", "leave", "close", "q"], "description": "Exit the program"},
    "help": {"keywords": ["help", "commands", "?"], "description": "Show available commands"},
    "clear": {"keywords": ["clear", "reset"], "description": "Clear the entire task list"}
}

# --- Colorizing Priority Labels ---
def color_priority(priority):
    if priority in ['h', 'high']:
        return COLOR_RED + 'HIGH' + COLOR_RESET
    elif priority in ['m', 'medium']:
        return COLOR_YELLOW + 'MEDIUM' + COLOR_RESET
    else:
        return COLOR_GREEN + 'LOW' + COLOR_RESET

# --- Maps input to command keys ---
def identify_command(user_input):
    user_input = user_input.lower()
    for cmd, data in todo_commands.items():
        if user_input in data['keywords']:
            return cmd
    return None

# --- Task Class: Represents a single task ---
class Task:
    def __init__(self, task, status="not started", priority="low"):
        self.task = task
        self.status = status
        self.priority = priority

    def to_dict(self):
        # Convert task to dictionary for JSON serialization
        return {
            "task": self.task,
            "status": self.status,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        # Convert dictionary to Task instance
        return Task(
            task=data.get("task", ""),
            status=data.get("status", "not started"),
            priority=data.get("priority", "low")
        )

# --- ToDoList Class: Manages collection of tasks ---
class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load()

    def load(self):
        # Load from file or return default list
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
        return [
            Task("buy milk", "complete", "low"),
            Task("do laundry", "not started", "low")
        ]

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)
        print("List saved!")

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task.task}" added.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f'Removed: {removed.task}')
        else:
            print("Invalid index")

    def clear_tasks(self):
        self.tasks.clear()

    def display(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("\nCurrent To-Do List:")
        for i, task in enumerate(self.tasks):
            print(f"- {i + 1}: {task.task} ({task.status}) [{color_priority(task.priority)}]")
        print()

# --- ToDoApp Class: Handles user interface and command loop ---
class ToDoApp:
    def __init__(self):
        self.todo_list = ToDoList()

    def run(self):
        print("Welcome to your to-do list!")
        while True:
            user_input = input("Enter a task or command: ").strip()
            if not user_input:
                print("Empty input. Try again.")
                continue

            command = identify_command(user_input.lower())

            if command == 'done':
                if input("Are you sure you want to quit? (y/n): ").lower() in ['y', 'yes']:
                    break
            elif command == 'list':
                self.todo_list.display()
            elif command == 'add':
                self.handle_add()
            elif command == 'remove':
                self.handle_remove()
            elif command == 'clear':
                self.todo_list.clear_tasks()
                self.todo_list.save()
            elif command == 'edit':
                self.handle_edit()
            elif command == 'save':
                self.todo_list.save()
            elif command == 'help':
                self.show_help()
            else:
                self.handle_add(user_input)

    def handle_add(self, name=None):
        task_name = name or input("Task name: ").strip()
        status = self.ask_status()
        priority = self.ask_priority()
        new_task = Task(task_name, status, priority)
        self.todo_list.add_task(new_task)
        self.todo_list.save()

    def handle_remove(self):
        self.todo_list.display()
        try:
            index = int(input("Task number to remove: ")) - 1
            self.todo_list.remove_task(index)
            self.todo_list.save()
        except ValueError:
            print("Invalid number.")

    def handle_edit(self):
        self.todo_list.display()
        try:
            index = int(input("Task number to edit: ")) - 1
            task = self.todo_list.tasks[index]
            field = input("Edit 'name', 'status', or 'priority': ").strip().lower()
            if field == 'name':
                task.task = input("New name: ").strip()
            elif field == 'status':
                task.status = self.ask_status()
            elif field == 'priority':
                task.priority = self.ask_priority()
            else:
                print("Invalid field.")
            self.todo_list.save()
        except (ValueError, IndexError):
            print("Invalid task number.")

    def show_help(self):
        print("\nAvailable Commands:")
        for command, data in todo_commands.items():
            keywords = ', '.join(data["keywords"])
            print(f'{command.upper():<10} - {data["description"]} (aliases: {keywords})')
        print()

    def ask_status(self):
        status_input = input("Status (complete/in progress/not started): ").strip().lower()
        status_map = {
            'done': 'complete', 'd': 'complete', 'c': 'complete', 'complete': 'complete',
            'ip': 'in progress', 'in progress': 'in progress', 'started': 'in progress', 's': 'in progress',
            'not started': 'not started', 'ns': 'not started'
        }
        return status_map.get(status_input, 'not started')

    def ask_priority(self):
        priority_input = input("Priority (high/medium/low) [default low]: ").strip().lower()
        priority_map = {
            'h': 'high', 'high': 'high',
            'm': 'medium', 'medium': 'medium',
            'l': 'low', 'low': 'low',
            '': 'low'
        }
        return priority_map.get(priority_input, 'low')

# --- Entry Point ---
if __name__ == "__main__":
    app = ToDoApp()
    app.run()
