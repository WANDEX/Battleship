#!/usr/bin/env python
from string import ascii_uppercase, digits
#from numpy import matrixlib

digits = list(digits)
digits.append('10')


def prnt_cells():  # dictionary's for col's
    col_A = {'A':1, 'A':2, 'A':3, 'A':4, 'A':5, 'A':6, 'A':7, 'A':8, 'A':9, 'A':10}
    col_B = {'B':1, 'B':2, 'B':3, 'B':4, 'B':5, 'B':6, 'B':7, 'B':8, 'B':9, 'B':10}
    col_C = {'C':1, 'C':2, 'C':3, 'C':4, 'C':5, 'C':6, 'C':7, 'C':8, 'C':9, 'C':10}
    col_D = {'D':1, 'D':2, 'D':3, 'D':4, 'D':5, 'D':6, 'D':7, 'D':8, 'D':9, 'D':10}
    col_E = {'E':1, 'E':2, 'E':3, 'E':4, 'E':5, 'E':6, 'E':7, 'E':8, 'E':9, 'E':10}
    col_F = {'F':1, 'F':2, 'F':3, 'F':4, 'F':5, 'F':6, 'F':7, 'F':8, 'F':9, 'F':10}
    col_G = {'G':1, 'G':2, 'G':3, 'G':4, 'G':5, 'G':6, 'G':7, 'G':8, 'G':9, 'G':10}
    col_H = {'H':1, 'H':2, 'H':3, 'H':4, 'H':5, 'H':6, 'H':7, 'H':8, 'H':9, 'H':10}
    col_I = {'I':1, 'I':2, 'I':3, 'I':4, 'I':5, 'I':6, 'I':7, 'I':8, 'I':9, 'I':10}
    col_J = {'J':1, 'J':2, 'J':3, 'J':4, 'J':5, 'J':6, 'J':7, 'J':8, 'J':9, 'J':10}
    print(col_A.iteritems)


def game_board():
    # print(ascii_uppercase[:10], end="\n")
    for simbol in ascii_uppercase[:10]:  # iterate ["A"-"J"]
        print(simbol, end=" ")  # print ["A"-"J"]
    print()
    prnt_cells()
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
