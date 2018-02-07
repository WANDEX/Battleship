#!/usr/bin/env python
from random import randint


turn = 0

def draw_cells():
    A = '\t'.expandtabs(3) + 'A'
    letters = [A, 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = range(1, 11)
    for x in letters:
        print(x, end='')

    print('')
    col = 'o' * 10

    for y in numbers:
        print(str(y) + '\t'.expandtabs(2) + (col))


def input_turn():
    print()
    print('col: ')
    x = input()
    print('row: ')
    y = input()

    print('turn is: x = {0} y = {1}'.format(x, y))


#draw_cells()
#input_turn()


board = []  # list


for x in range(10):
    board.append(list(str(x + 1) + '|') + ["O"] * 10)


def print_letters():
    A = '\t'.expandtabs(4) + 'A'
    letters = [A, 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for x in letters:
        print(x, end=' ')
    print()


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print("THE TURN #: {0}".format(turn + 1))
print_letters()
print_board(board)
print('\n' + str(ship_row))
print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
while turn < 5:
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) + 1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
    else:
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print()
        #print("THE TURN #: {0}".format(turn + 1))
        print("THE TURN #: " + str(turn + 1))
        print_letters()
        print_board(board)
