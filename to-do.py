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

    elif add_to_list == 'remove':
        for x, task in enumerate(todo):
            print(f'- {x}: {task["task"]} ({task["status"]})')
        try:
            task_index = int(input('Enter the index of the task you want removed: '))
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue
        if task_index > len(todo) - 1 or task_index < 0:
            print('Invalid task index')
            continue
        try:
            inp = input(f'Are you sure you want to delete {task_index}: "{todo[task_index]["task"]}"? ').strip().lower()
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

    # Ask for task status
    status_input = input('What is the status of this task? (complete/in progress/not started): ').strip().lower()
    if status_input not in ['complete', 'in progress', 'not started']:
        print('Invalid status. Defaulting to "not started".')
        status_input = 'not started'

    # Add task as a dictionary with status
    todo.append({
        'task': add_to_list,
        'status': status_input
    })
    print(f'"{add_to_list}" has been added to the list with status: {status_input}')
    save_list()

    print('\nCurrent To-Do List:')
    for x, task in enumerate(todo):
        print(f'- {x}: {task["task"]} ({task["status"]})')
