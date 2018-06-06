#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Board class."""


class Board(object):
    def __init__(self, owner):
        self.owner = owner
        print("Hi {0}.".format(self.owner))
        self.grid = []
        self.ships = []
        self.width = 11
        self.height = 11
