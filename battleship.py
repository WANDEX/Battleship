#!/usr/bin/env python
from string import ascii_uppercase, digits
#from numpy import matrixlib

digits = list(digits)
digits.append('10')


def prnt_cells():  # col's dictionary's
    print("quack")
    col_headers = ["col{}".format(i) for i in range(1, 4)]
    print("{:^8} {:^8} {:^8}".format(*col_headers))
    print(digits, sep='\n')
    # for row in digits:
    #     aligned_row = "{:^8} {:^8} {:^8}".format(*row)
    #     print(aligned_row)

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
