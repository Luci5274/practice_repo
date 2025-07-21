import json
import os

todo_commands = {
    "add": {
        "keywords": ["add", "new", "create"],
        "description": "Add a new task to the list"
    },
    "remove": {
        "keywords": ["remove", "delete", "rm"],
        "description": "Delete a task from the list"
    },
    "list": {
        "keywords": ["list", "show list", "ls", "sl", "l"],
        "description": "Show the full list of tasks"
    },
    "edit": {
        "keywords": ["edit", "update", "change"],
        "description": "Edit an existing task's text or status"
    },
    "save": {
        "keywords": ["save", "write"],
        "description": "Save the current list to file"
    },
    "done": {
        "keywords": ["done", "exit", "quit", "leave", "close"],
        "description": "Exit the program"
    },
    "help": {
        "keywords": ["help", "commands", "?"],
        "description": "Show available commands"
    },
    "filter": {
        "keywords": ["filter", "search"],
        "description": "Filter tasks by status (e.g., completed, in progress)"
    },
    "sort": {
        "keywords": ["sort", "order"],
        "description": "Sort tasks alphabetically or by status"
    },
    "clear": {
        "keywords": ["clear", "reset"],
        "description": "Clear the entire task list (with confirmation)"
    }
}

def save_list():
    with open('todo.json', 'w') as file:
        json.dump(todo, file)
    print('List Saved!')

if os.path.exists('todo.json'):
    with open('todo.json', 'r') as f:
        todo = json.load(f)
else:
    todo = [
        {'task': 'buy milk', 'status': 'complete'},
        {'task': 'do laundry', 'status': 'not started'}
    ]

def display_list():
    for x, task in enumerate(todo):
        print(f'- {x + 1}: {task["task"]} ({task["status"]})')

def to_do_list():
    print('Welcome to your to-do list!')
    print('Commands: [task name], "list", "remove", "edit", "save", "done", "help"')

def ask_status():
    status_input = input('What is the status of this task? (complete/in progress/not started): ').strip().lower()

    status_map = {
        'done': 'complete', 'd': 'complete', 'c': 'complete', 'complete': 'complete',
        'ip': 'in progress', 'in progress': 'in progress', 'started': 'in progress', 's': 'in progress',
        'not started': 'not started', 'ns': 'not started'
    }

    if status_input not in status_map:
        print('Invalid status. Defaulting to "not started".')

    return status_map.get(status_input, 'not started')

to_do_list()

while True:
    add_to_list = input('Input a task (or type "done" to finish): ').strip().lower()

    if add_to_list == 'done':
        conf = input('Are you sure? (yes/no): ').strip().lower()
        if conf in ['yes', 'y']:
            break
        else:
            continue

    if add_to_list in ['show list', 'list', 'l', 'sl', 'ls']:
        display_list()
        continue

    elif add_to_list in ['help', 'h', '?']:
        print('\nAvailable Commands:')
        for command, data in todo_commands.items():
            keywords = ', '.join(data["keywords"])
            print(f'{command.upper():<10} - {data["description"]} (aliases: {keywords})')
        print()
        continue

    elif add_to_list in ['remove', 'delete']:
        display_list()
        try:
            task_index = int(input('Enter the task number you want removed: ')) - 1
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue
        if task_index < 0 or task_index >= len(todo):
            print('Invalid task number')
            continue
        try:
            inp = input(f'Are you sure you want to delete {task_index + 1}: "{todo[task_index]["task"]}"? (y/n) ').strip().lower()
            if inp in ['y', 'yes']:
                del todo[task_index]
                print('Item has been successfully removed!')
                save_list()
            else:
                print('No deletions were made.')
        except IndexError as e:
            print("Index is out of range.")
            print(e)
        continue

    elif add_to_list in ['edit', 'change']:
        display_list()
        try:
            task_index = int(input('Enter the task number you want to edit: ')) - 1
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue
        if task_index < 0 or task_index >= len(todo):
            print('Invalid task number')
            continue

        field_to_edit = input('Edit task name or status? (type "name" or "status"): ').strip().lower()
        if field_to_edit in ['name', 'n']:
            new_name = input('Enter new task name: ').strip()
            todo[task_index]['task'] = new_name
            print('Task name updated.')
        elif field_to_edit in ['status', 's']:
            new_status = ask_status()
            todo[task_index]['status'] = new_status
            print('Task status updated.')
        else:
            print('Invalid choice, returning to main menu.')
            continue

        save_list()
        continue

    elif add_to_list == 'save':
        try:
            save_list()
            print('Your list has been saved!')
        except Exception as e:
            print('UH OH! Something went wrong')
            print(e)
        continue

    # Add new task
    status = ask_status()
    todo.append({
        'task': add_to_list,
        'status': status
    })
    print(f'"{add_to_list}" has been added to the list as: {status}')
    save_list()

    print('\nCurrent To-Do List:')
    display_list()
