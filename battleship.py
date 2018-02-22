#!/usr/bin/env python3
from random import randint
import ship

board = []  # list
ship_list = []


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


def random_row(board):  # избавиться т.к. есть generate_position()
    return randint(1, len(board))


def random_col(board):  # избавиться т.к. есть generate_position()
    return randint(1, len(board))


def generate_position(board):
    position = tuple()  # кортеж быстрее списка в 10 раз и является неизменным
    position = randint(1, len(board)), randint(1, len(board))
    return position


def create_ship(s, length, name):
    s = ship.Ship(length, name)
    ship_list.append(s)
    return(s.name)


def create_ships():
    create_ship(s='s', length=1, name='Submarine')
    create_ship(s='f', length=4, name='Battleship')
    fleet_positioning(ship_list)
    print("SHIPS CREATED SUCCESSFULLY, THANKS LORD!!!")


def fleet_positioning(ship_list):  # list of ships as fleet = [s1, s2, s3, s4]
    for ship_item in ship_list:
        ship_item.loc = generate_position(board)
        print("added {0} at position {1}".format(ship_item.name, ship_item.loc))


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


def main():  # main
    gamecycle()  # start game cycle

    create_ships()


main()
