import json
import os

def save_list():
    with open('todo.json','w')as file:
        json.dump(todo, file)
    print('List Saved!')

if os.path.exists('todo.json'):
    with open ('todo.json','r') as f:
        todo = json.load(f)
else:
    todo = []

def to_do_list():
    print('Welcome to your to-do list!')

to_do_list()

while True:
    add_to_list = input('Input a task (or type "done" to finish): ').strip().lower()

    if add_to_list == 'done':
        conf = input('are you sure?: ').strip().lower()
        if conf in ['yes', 'y']:
            break
        else:
            continue


    elif add_to_list == 'remove':
        for x, task in enumerate(todo):
            print(f'- {x}: {task}')
        try:
            task_index = int(input('Enter the index of the task you want removed:'))
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue  # Important to continue to skip deletion if input is invalid
        if task_index > len(todo) -1 or task_index < 0:
            print('invalid task index')
            continue
        try:
            inp = input(f'are you sure you want to delete {task_index}:"{todo[task_index]}"?').strip().lower()
            if inp in ['y','yes']:
                del todo[task_index]
                print('Item has been successfully removed!')
                save_list()
            else:
                print('entire list successfully deleted! \n jk, no deletions were made')
                continue
        except IndexError as e:
            print("Index is out of range.")
            print(e)
        continue

    elif add_to_list == 'save':
        try:
            save_list()
            print('your list has been saved!')
            continue
        except Exception as e:
            print('UH OH! something went wrong')
            print(e)

    todo.append(add_to_list)
    print(f'"{add_to_list}" has been added to the list!')
    save_list()


    print('\nCurrent To-Do List:')
    for x, task in enumerate(todo):
        print(f'- {x}: {task}')