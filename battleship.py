#!/usr/bin/env python3
from random import randint

board = []  # list

def append_board():
    for x in range(10):
        board.append(list(repr(x + 1).rjust(2) + '|') + ["O"] * 10)

def print_letters():
    A = '\t'.expandtabs(6) + 'A'
    letters = [A, 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for x in letters:
        print(x, end=' ')
    print('\n' + ' ' * 5 + "_" * 20)

def print_board(board):
    for row in board:
        print(" ".join(row))
    print('\n' + '#' * 80 + '\n')

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board))

def generate_1x(row, col):
    ship_row = row
    ship_col = col

    return ship_row, ship_col

def gamecycle():
    turn = 0
    append_board()
    # ship_row_1x = random_row(board)
    # ship_col_1x = random_col(board)
    ship_row_1x, ship_col_1x = generate_1x(random_row(board), random_col(board))

    while turn < 50:  # condition for game length
        turn = turn + 1
        print("THE TURN #: {0}".format(turn))
        print("row_1x: {0} col_1x: {1}".format(ship_row_1x, ship_col_1x))

        print_letters()
        print_board(board)

        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if ((guess_row < 1 or guess_row > 10) or
            (guess_col < 1 or guess_col > 10)):
            print("Oops, that's not even in the ocean.")
        elif guess_row == ship_row_1x and guess_col == ship_col_1x:
            print("Congratulations! You sunk my battleship!\n")
            board[guess_row - 1][guess_col + 2] = "X"
        else:
            guess_row = guess_row - 1
            guess_col = guess_col + 2
            if ((board[guess_row][guess_col] == ".") or
                (board[guess_row][guess_col] == "X")):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "."
            print()

def run():  # main
    gamecycle()  # start game cycle

run()
