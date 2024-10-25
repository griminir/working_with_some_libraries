from termcolor import colored

PLAYER_1 = 'X'
PLAYER_2 = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def cell(mark):
    color = 'red' if mark == PLAYER_1 else 'green'
    return colored(mark, color)


def print_board(board):
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ')
        print(line)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print('Not a valid position')


def get_player_move(current_player):
    print(f'player {current_player}\'s turn:')

    while True:
        row = get_position('chose row (0-2): ')
        column = get_position('chose column (0-2): ')

        if board[row][column] == ' ':
            board[row][column] = current_player
            break

        print('This spot is already taken')


def main():
    print_board(board)

    current_player = PLAYER_1

    while True:
        get_player_move(current_player)

        print_board(board)

        if check_winner(board):
            print(f'Contratulations {current_player}')
            break

        if is_full(board):
            print('Board is full it\'s a draw')
            break

        if current_player == PLAYER_1:
            current_player = PLAYER_2
        else:
            current_player = PLAYER_1
        # can also be written like current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
