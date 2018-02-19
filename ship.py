#!/usr/bin/env python3

class Ship:

    def __init__(self, length, name):
        self.length = length
        self.name = name
        self.sunk = False
        self.loc = []

    def __del__(self):
        pass
