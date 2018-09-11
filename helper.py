#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper class."""
from random import randint


class Helper(object):
    def set_ships(self, ship, grid):
        node = randint(1, len(grid) - 1)
        ship_length = ship.length
        horizontal = randint(0, 1)
        # check horizontal
        if horizontal:
            for i in range(ship_length):
                if grid[node + i].is_border or grid[node + i].has_ship:
                    self.set_ships(ship, grid)
                    break
            else:
                for i in range(ship_length):
                    grid[node + i].has_ship = True
                    grid[node + i].current_ship = ship.name
                    ship.loc.append(grid[node + i])
                print("your", ship.name, "placed")
        else:
            # check vertical
            for i in range(ship_length):
                if grid[node + (i * 11)].is_border or grid[node + (i * 11)].has_ship:
                    self.set_ships(ship, grid)
                    break
            else:
                for i in range(ship_length):
                    grid[node + (i * 12)].has_ship = True
                    grid[node + (i * 12)].current_ship = ship.name
                    ship.loc.append(grid[node + (i * 12)])
                print("your", ship.name, "placed")

    def tile_check(self, player, x, y):  # TODO <----------
        print(player)
        exit()
