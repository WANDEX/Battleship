#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
from random import randint
import ship
import players
import board
import tiles

ship_list = []


def player():
    name = "PlayerName"
    # name = input("name: ")
    player = players.Player(name)
    player.board = board.Board(name)
    player.board.grid = gen_board(player)
    player.board.ships = fleet()
    print("setting ships for", player.name)
    return name


def gen_board(player):
    grid = []
    tile_num = 0
    width = player.board.width
    height = player.board.height
    for y in range(width + 1):
        for x in range(height + 1):
            tile = tiles.Tile(tile_num, x, y)
            if(tile_num < width + 1) or (x % width == 0) or (y % height == 0):
                tile.is_border = True
            grid.append(tile)
            tile_num += 1
    return grid


def get_ships(player):
    ships = [ship.Ship(4, "Battleship", gen_loc(player)),
             ship.Ship(3, "Battleship", gen_loc(player)),
             ship.Ship(2, "Battleship", gen_loc(player)),
             ship.Ship(1, "Battleship", gen_loc(player))]
    print(ships)
    return ships


def gen_loc(player):
    loc = randint(1, player.board.width), randint(1, player.board.height)
    return loc


def fleet():
    # instantiate_s(length=1, name='Submarine', loc=gen_loc(board))
    # instantiate_s(length=4, name='Battleship')
    for s in ship_list:
        print("added {0} at position {1}, his length is {2}".format(s.name, s.loc, s.length))
    print("SHIPS CREATED, THANKS LORD!!!")
    return ship_list


def game():
    player = player()
    gen_board(player)
    # fleet()


game()
