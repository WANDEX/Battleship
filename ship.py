#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ship class."""


class Ship(object):
    def __init__(self, length, name):
        self.length = length
        self.name = name
        self.loc = []
        self.sunk = False

    def __del__(self):
        pass
