def basic_calc():
    x = float(input('Enter your first number: '))
    op = str(input('Add your operator (-, +, /, *): '))
    y = float(input('Enter your second number: '))

    if op in ['*', '+', '-', '/']:
        if op == '+':
            fin = x + y
        elif op == '-':
            fin = x - y
        elif op == '*':
            fin = x * y
        elif op == '/':
            try:
                fin = x / y
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                return  # Exit early to avoid printing an undefined result
        print(f'{x} {op} {y} = {fin}!')
    else:
        print(f"Error: '{op}' is not a valid operator.")

while True:
    basic_calc()

    replay = input('do you want to go again? (Y/N): ').strip().upper()
    if replay not in ['y','yes']:
        print('goodbye')
        break