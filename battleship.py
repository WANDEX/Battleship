#!/usr/bin/env python3
from random import randint
import ship

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


# def create_ships():
#     s1 = ship.Ship(generate_position)
#     s2 = ship.Ship(generate_position)
#     s3 = ship.Ship(generate_position)
#     s4 = ship.Ship(generate_position)
#     fleet = [s1, s2, s3, s4]
#     return fleet






def ship_positioning(ship_object):
    current_ship = ship.Ship(ship_object, random_row(board), random_col(board))
    print(current_ship)
    return(current_ship)


def create_single_decker():
    single_decker = ship_positioning(ship.Ship.single_decker(ship))
    print(single_decker)
    return(single_decker)


def create_ships():
    create_single_decker()
    create_single_decker()
    print("SHIPS CREATED SUCCESSFULLY, THANKS LORD!!!")


def fleet_positioning(ship_list):  # list of ships as fleet = [s1, s2, s3, s4]
    for ship_item in ship_list:
        ship_positioning(ship_item)
        print("added {0} position".format(ship_item))







def gamecycle():
    turn = 0
    append_board()
    # ship_row_1x = random_row(board)
    # ship_col_1x = random_col(board)
    ship_row_1x, ship_col_1x = random_row(board), random_col(board)

    while turn < 1:  # condition for game length
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

    create_ships()

run()
