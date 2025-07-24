import json
import os

# --- Command dictionary ---
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
        "description": "Edit an existing task's text, status, or priority"
    },
    "save": {
        "keywords": ["save", "write"],
        "description": "Save the current list to file"
    },
    "done": {
        "keywords": ["done", "exit", "quit", "leave", "close", "q"],
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

# --- ANSI Color Codes ---
COLOR_RESET = '\033[0m'
COLOR_RED = '\033[91m'
COLOR_YELLOW = '\033[93m'
COLOR_GREEN = '\033[92m'

def color_priority(priority):
    if priority in ['h', 'high']:
        return COLOR_RED + 'HIGH' + COLOR_RESET
    elif priority in ['medium', 'm']:
        return COLOR_YELLOW + 'MEDIUM' + COLOR_RESET
    else:
        return COLOR_GREEN + 'LOW' + COLOR_RESET

def identify_command(user_input):
    user_input = user_input.lower()
    for cmd, data in todo_commands.items():
        if user_input in data['keywords']:
            return cmd
    return None

def save_list():
    with open('todo.json', 'w') as file:
        json.dump(todo, file, indent=2)
    print('List saved!')

def load_or_create_todo():
    if os.path.exists('todo.json'):
        with open('todo.json', 'r') as f:
            return json.load(f)
    else:
        return [
            {'task': 'buy milk', 'status': 'complete', 'priority': 'low'},
            {'task': 'do laundry', 'status': 'not started', 'priority': 'low'}
        ]

def display_list():
    if not todo:
        print("Your to-do list is empty.")
        return
    print("\nCurrent To-Do List:")
    for idx, task in enumerate(todo):
        task_name = task.get("task", "")
        task_status = task.get("status", "not started")
        priority_raw = task.get("priority", "low")  # fallback for older tasks
        priority_display = color_priority(priority_raw)
        print(f'- {idx + 1}: {task_name} ({task_status}) [{priority_display}]')
    print()

def welcome():
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

def ask_priority():
    priority_input = input('Set task priority (high/medium/low) [default low]: ').strip().lower()
    valid_priorities = {
        'h': 'high', 'high': 'high',
        'm': 'medium', 'medium': 'medium',
        'l': 'low', 'low': 'low',
        '': 'low'
    }
    if priority_input not in valid_priorities:
        print('Invalid priority. Defaulting to "low".')
        return 'low'
    return valid_priorities[priority_input]

def show_help():
    print('\nAvailable Commands:')
    for command, data in todo_commands.items():
        keywords = ', '.join(data["keywords"])
        print(f'{command.upper():<10} - {data["description"]} (aliases: {keywords})')
    print()

def handle_add(user_input):
    status = ask_status()
    priority = ask_priority()
    todo.append({'task': user_input, 'status': status, 'priority': priority})
    print(f'"{user_input}" added to the list as: {status} with priority: {priority}')
    save_list()
    display_list()

def handle_remove():
    if not todo:
        print("Your list is already empty.")
        return
    display_list()
    try:
        task_index = int(input('Enter the task number you want removed: ')) - 1
        if 0 <= task_index < len(todo):
            confirm = input(f'Delete {task_index + 1}: "{todo[task_index]["task"]}"? (y/n): ').strip().lower()
            if confirm in ['y', 'yes']:
                del todo[task_index]
                print('Item removed!')
                save_list()
                display_list()
            else:
                print('No deletions made.')
        else:
            print('Invalid task number.')
    except (ValueError, IndexError) as e:
        print(f'Error: {e}')

def handle_clear():
    if not todo:
        print('Your list is already empty.')
        return

    print(
        '\n****WARNING****\n'
        'THIS WILL CLEAR YOUR LIST\n'
        '****WARNING****\n'
    )
    confirm = input('Are you sure (Y)es/(N)o?: ').strip().lower()

    if confirm in ['yes', 'y']:
        todo.clear()
        save_list()
        print('All tasks have been successfully cleared!')
    else:
        print("Clear operation canceled.")

def handle_edit():
    if not todo:
        print("Your list is empty. Nothing to edit.")
        return
    display_list()
    try:
        task_index = int(input('Enter the task number to edit: ')) - 1
        if 0 <= task_index < len(todo):
            field_to_edit = input('Edit task name, status, or priority? (type "name", "status", or "priority"): ').strip().lower()
            if field_to_edit in ['name', 'n']:
                new_name = input('Enter new task name: ').strip()
                if new_name:
                    todo[task_index]['task'] = new_name
                    print('Task name updated.')
                else:
                    print('Task name cannot be empty.')
            elif field_to_edit in ['status', 's', 'stat', 'stats']:
                new_status = ask_status()
                todo[task_index]['status'] = new_status
                print('Task status updated.')
            elif field_to_edit in ['priority', 'p']:
                new_priority = ask_priority()
                todo[task_index]['priority'] = new_priority
                print('Task priority updated.')
            else:
                print('Invalid choice.')
            save_list()
            display_list()
        else:
            print('Invalid task number.')
    except (ValueError, IndexError) as e:
        print(f'Error: {e}')

def main_loop():
    welcome()
    while True:
        raw_input_text = input('Input a task (or type "done" to finish): ').strip()
        user_input = raw_input_text.lower()
        command_key = identify_command(user_input)

        if command_key == 'done':
            conf = input('Are you sure? (yes/no): ').strip().lower()
            if conf in ['yes', 'y']:
                print("Goodbye!")
                break
            else:
                continue
        elif command_key == 'list':
            display_list()
        elif command_key == 'help':
            show_help()
        elif command_key == 'remove':
            handle_remove()
        elif command_key == 'clear':
            handle_clear()
        elif command_key == 'edit':
            handle_edit()
        elif command_key == 'save':
            try:
                save_list()
                print('Your list has been saved!')
            except Exception as e:
                print('UH OH! Something went wrong.')
                print(e)
        elif user_input.isdigit():
            task_index = int(user_input) - 1
            if 0 <= task_index < len(todo):
                todo[task_index]['status'] = 'complete'
                print(f'Task {task_index + 1} marked as complete.')
                save_list()
                display_list()
            else:
                print('Invalid task number.')
        else:
            # Treat input as a new task
            if raw_input_text == '':
                print("Please enter a valid task name or command.")
            else:
                handle_add(raw_input_text)

# --- Entry point ---
if __name__ == "__main__":
    todo = load_or_create_todo()
    main_loop()
