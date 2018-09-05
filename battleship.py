#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
from random import randint
import ship
import players
import board
import tiles

ship_list = []


def get_player():
    name = input("what\'s your name?: ") or "Player"
    return name


def get_board(player):
    grid = []
    tile_num = 0


    # brd = board.Board(player)

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
             ship.Ship(3, "Cruiser", gen_loc(player)),
             ship.Ship(2, "Submarine", gen_loc(player)),
             ship.Ship(1, "Destroyer", gen_loc(player))]
    print(ships)
    return ships


def gen_loc(player):
    brd = board.Board(player)

    loc = randint(1, brd.width), randint(1, brd.height)
    return loc


def run():
    p1_name = get_player()
    p1 = players.Player(p1_name)
    p1.board = board.Board(p1_name)
    p1.board.grid = get_board(p1)
    print ("setting ships for", p1.name)
    # set_ships(p1.board)

    p1_board = get_board(p1)
    print(p1_board)


run()
