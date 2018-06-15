#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
from random import randint
import ship
import players
import board
import tiles

ship_list = []


# not tested at all
def get_player():
    name = "PlayerName"
    # name = input("name: ")
    player = players.Player(name)

    brd = board.Board(player)

    brd.owner = board.Board(name)
    brd.grid = get_board(player)
    brd.ships = get_ships(player)
    print("setting ships for", player.name)
    return player


def get_board(player):
    grid = []
    tile_num = 0

    brd = board.Board(player)

    width = brd.width
    height = brd.height

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
             ship.Ship(3, "Cruiser", gen_loc(player)),
             ship.Ship(2, "Submarine", gen_loc(player)),
             ship.Ship(1, "Destroyer", gen_loc(player))]
    print(ships)
    return ships


def gen_loc(player):
    brd = board.Board(player)

    loc = randint(1, brd.width), randint(1, brd.height)
    return loc


def game():
    # get_player()
    p = players.Player(get_player())
    # fleet()


game()
