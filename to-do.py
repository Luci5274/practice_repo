todo = []

def to_do_list():
    print('Welcome to your to-do list!')

to_do_list()

while True:
    add_to_list = input('Input a task (or type "done" to finish): ').strip().lower()

    if add_to_list == 'done':
        print('Goodbye!')
        break
    elif add_to_list == 'remove':
        for x, task in enumerate(todo):
            print(f'- {x}: {task}')
        try:
            task_index = int(input('...'))
        except ValueError as e:
            print("Input is not a valid integer.")
            print(e)
            continue  # Important to continue to skip deletion if input is invalid

        try:
            del todo[task_index]
        except IndexError as e:
            print("Index is out of range.")
            print(e)
        continue

    todo.append(add_to_list)
    print(f'"{add_to_list}" has been added to the list!')


    print('\nCurrent To-Do List:')
    for x, task in enumerate(todo):
        print(f'- {x}: {task}')