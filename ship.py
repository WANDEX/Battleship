#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ship class."""


class Ship:
    def __init__(self, length, name, loc):
        self.length = length
        self.name = name
        self.loc = []
        self.sunk = False

    def __del__(self):
        pass
