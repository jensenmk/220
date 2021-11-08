"""
Name: Mark Jensen
lab10.py
"""


def build_board():
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return position_list


def display_board(position_list):
    print('-------------')
    counter = 0
    for i in range(3):
        print(' |', end='')
        for j in range(3):
            print(position_list[counter], end=' | ')
            counter = counter + 1
        print('\n' + '-' * 13)


def place_spot(position_list, spot, marker):
    position_list[spot] = marker


def legal_spot(board, spot):
    if (board[spot] == 'X' or board[spot] == 'O') or (spot < 0 or spot > 9):
        return False
    else:
        return True


def game_won(board):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for condition in win_con:
        counter = 0
        for spot in condition:
            if board[spot - 1] == 'X':
                counter = counter + 1
            if counter == 3:
                return "X wins"
    for condition in win_con:
        counter = 0
        for spot in condition:
            if board[spot - 1] == 'O':
                counter = counter + 1
            if counter == 3:
                return "O wins"


def game_over(board, turn_count):
    if (game_won(board) == "X wins" or game_won(board) == "O wins") or (turn_count > 9):
        return True
    else:
        return False


def play_game():
    board = build_board()
    display_board(board)
    count = 1
    while not game_over(board, count):
        spot = int(input('enter X position: '))
        marker = "X"
        spot = spot - 1
        if legal_spot(board, spot):
            place_spot(board, spot, marker)
            display_board(board)
        if game_won(board) == 'X wins':
            print('X wins')
            break
        count = count + 1
        spot = int(input('enter O position: '))
        spot = spot - 1
        marker = "O"
        if legal_spot(board, spot):
            place_spot(board, spot, marker)
            display_board(board)
        if game_won(board) == 'O wins':
            print('O wins')
        count = count + 1
    else:
        print('tie')





play_game()