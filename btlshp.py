#!/usr/bin/env python


def draw_cells():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = range(1, 10)
    for x in letters:
        print(x, end=' ')

    print('')
    for y in numbers:
        print(y)


draw_cells()
