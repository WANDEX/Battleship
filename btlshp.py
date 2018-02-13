#!/usr/bin/env python
from random import randint


turn = 0


board = []  # list


for x in range(10):
    board.append(list(repr(x + 1).rjust(2) + '|') + ["O"] * 10)
    #board.append(["O"] * 10)


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
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
while turn < 5:
    turn = turn + 1
    print("THE TURN #: {0}".format(turn))
    print("row: {0} col: {1}".format(ship_row, ship_col))

    print_letters()
    print_board(board)

    guess_row = int(input("Guess Row: ")) #- 1
    guess_col = int(input("Guess Col: ")) #+ 2

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row - 1][guess_col + 2] = "X"
    else:
        if((guess_row < 0 or guess_row > 10) or
           (guess_col < 0 or guess_col > 10)):
            print("Oops, that's not even in the ocean.")
        elif((board[guess_row - 1][guess_col + 2] == ".") or
             (board[guess_row - 1][guess_col + 2] == "X")):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row - 1][guess_col + 2] = "."
        print()
