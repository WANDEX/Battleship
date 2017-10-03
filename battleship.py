#!/usr/bin/env python
from string import ascii_uppercase, digits
#from numpy import matrixlib

digits = list(digits)
digits.append('10')


def prnt_cells():  # col's dictionary's
    col_A = {
        'A': 1,
        'A': 2,
        'A': 3,
        'A': 4,
        'A': 5,
        'A': 6,
        'A': 7,
        'A': 8,
        'A': 9,
        'A': 10
    }

    for col in sorted(set(col_A.items())):
        print(col)
    return col_A




def game_board():
    # print(ascii_uppercase[:10], end="\n")
    for simbol in ascii_uppercase[:10]:  # iterate ["A"-"J"]
        print(simbol, end=" ")  # print ["A"-"J"]
    print()
    print(prnt_cells())
    # for simbol in digits[1:]:
    #     print(simbol + "* * * * * * * * * *", sep=' ')
    #for y in range(10):
    #print(digits[1:])


def game_loop():
    screen_refresh_count = 1
    print("screen refreshed | count: " + str(screen_refresh_count) + "\n")

    game_board()

    screen_refresh_count += 1
    print("\nend of the game screen")  # end of function


game_loop()
