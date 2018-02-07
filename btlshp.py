#!/usr/bin/env python


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

    print('turn is: x = {} y = {}'.format(x, y))


draw_cells()
input_turn()
