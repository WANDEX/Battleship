#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tile class."""


class Tile(object):
    def __init__(self, number, row, column):
        self.number = number
        self.row = row
        self.column = column
        self.is_border = False
        self.has_ship = False
        self.bombed = False
        self.current_ship = "nothing but the deep blue sea here"
