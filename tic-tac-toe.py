board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(f'{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}')
        if i < 2:
            print('---|---|---')
    print()

def get_player_move(player):
    while True:
        try:
            move =int(input(f'player {player}, choose a position (1-9): ')) -1

            if move >= 0 and move < 9 and board[move] ==' ':
                return move
            else:
                print('Invalid move. cell is taken or out of range')
        except ValueError:
            print('try agin, bihh (1-9)')

def check_winner(player):
    win_combo =  [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in win_combo:
        if all(board[i] ==player for i in combo):
            return True
        return False

def is_draw():
    print('Draw!')
    return ' ' not in board

def play_game():
    current_player = 'X'
    while True:
        print_board()

        move = get_player_move(current_player)
        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f'Player {current_player} wins!')

        elif is_draw():
            print_board()
            break

        current_player = 'O' if current_player =="X" else "X"

if __name__ == '__main__':
    play_game()