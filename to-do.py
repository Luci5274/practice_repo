import json
import os


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

def displaylist(todo):
    for x, task in enumerate(todo):
        print(f'- {x + 1}: {task["task"]} ({task["status"]})')

def to_do_list():
    print('Welcome to your to-do list!')

to_do_list()

while True:
    add_to_list = input('Input a task (or type "done" to finish): ').strip().lower()

    if add_to_list == 'done':
        conf = input('Are you sure?: ').strip().lower()
        if conf in ['yes', 'y']:
            break
        else:
            continue

    # ✅ FIXED: Missing colon added
    if add_to_list in ['show list', 'list', 'l', 'sl', 'ls']:
        displaylist()
        continue

    elif add_to_list in ['remove', 'delete']:
        for x, task in enumerate(todo):
            print(f'- {x+1}: {task["task"]} ({task["status"]})')
        try:
            # ✅ FIXED: Subtract 1 from user-friendly index
            task_index = int(input('Enter the task number you want removed (starting from 1): ')) - 1
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue
        if task_index > len(todo) - 1 or task_index < 0:
            print('Invalid task number')
            continue
        try:
            inp = input(f'Are you sure you want to delete {task_index + 1}: "{todo[task_index]["task"]}"? ').strip().lower()
            if inp in ['y', 'yes']:
                del todo[task_index]
                print('Item has been successfully removed!')
                save_list()
            else:
                print('No deletions were made.')
                continue
        except IndexError as e:
            print("Index is out of range.")
            print(e)
        continue

    elif add_to_list == 'save':
        try:
            save_list()
            print('Your list has been saved!')
            continue
        except Exception as e:
            print('UH OH! Something went wrong')
            print(e)
            continue

    status_input = input('What is the status of this task? (complete/in progress/not started): ').strip().lower()

    # Map shortcuts to full labels
    status_map = {
        'done': 'complete', 'd': 'complete', 'c': 'complete', 'complete': 'complete',
        'ip': 'in progress', 'in progress': 'in progress', 'started': 'in progress', 's': 'in progress',
        'not started': 'not started', 'ns': 'not started'
    }

    status = status_map.get(status_input, 'not started')
    if status_input not in status_map:
        print('Invalid status. Defaulting to "not started".')

    # Add task with normalized status
    todo.append({
        'task': add_to_list,
        'status': status
    })
    print(f'"{add_to_list}" has been added to the list with status: {status}')
    save_list()

    print('\nCurrent To-Do List:')
    for x, task in enumerate(todo):
        print(f'- {x+1}: {task["task"]} ({task["status"]})')
