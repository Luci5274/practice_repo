import random
import sys

def die():
    """DOCSTRING
        Prompt user for a number and roll a die with that many sides (1–100).
        Accepts "done" to exit."""
    inp = input('enter a number, or "done": ')
    if inp in ['done', 'd']:
        print('goodbye')
        sys.exit()
    try:
        x = int(inp)
    except ValueError:
        print(f' {inp} not an integer')
        print('Summoning the porcelain babies')
        return
    if x not in range(1, 101):
        print(f'your input:{x}, has been rejected, dropping the nukes')
        print('please enter a whole number between 1 and 100... if you survive')
    else:
        roll = random.randrange(1, x + 1)
        print(f'your roll is: {roll}')
        return
while True:
    die()
    confirm = input('would you like to roll again? (Y/N): ').strip().lower()
    if confirm not in ['y','yes']:
        print('goodbye, and run! RUN BEFORE THEY CATCH YOU!')
        sys.exit()
