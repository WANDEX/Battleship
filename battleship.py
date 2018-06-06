#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
from random import randint
import ship

board = []
ship_list = []


def gen_board(board):
    pass


def gen_loc(board):
    loc = randint(1, len(board)), randint(1, len(board))
    return loc


def instantiate_s(length, name, loc):
    s = ship.Ship(length, name, loc)
    ship_list.append(s)
    return(s)


def fleet():
    sub_1 = instantiate_s(length=1, name='Submarine', loc=gen_loc(board))
    # instantiate_s(length=4, name='Battleship')
    for s in ship_list:
        print("added {0} at position {1}, his length is {2}".format(s.name, s.loc, s.length))
    print("SHIPS CREATED, THANKS LORD!!!")


# def fleet_pos(ship_list):  # list of ships as fleet = [s1, s2, s3, s4]
#     
#         print("added {0} at position {1}".format(s.name, s.loc))

def game():
    gen_board(board)
    # fleet()
