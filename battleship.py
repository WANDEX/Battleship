#!/usr/bin/env python
from string import ascii_uppercase, digits

digits = list(digits)
digits.append('10')


def game_board():
    # print(ascii_uppercase[:10], end="\n")
    for simbol in ascii_uppercase[:10]:  # ["A"-"J"]
        print(" " + simbol, end="")
    print()
    for simbol in digits[1:]:
        print(simbol + "* * * * * * * * * *", sep=' ')


    # for si


def game_loop():
    screen_refresh_count = 1
    print("screen refreshed | count: " + str(screen_refresh_count) + "\n")

    game_board()

    screen_refresh_count += 1
    print("\nend of the game screen")  # end of function


game_loop()
