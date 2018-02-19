#!/usr/bin/env python3

class Ship:

    def __init__(self, length, name):
        self.length = length
        self.name = name
        self.sunk = False
        self.loc = []

    def __del__(self):
        pass

    # def four_decker(self):
    #     ship_name = 'Battleship'
    #     ship_length = 4
    #     amount = 1
    #     return ship_name, ship_length, amount
    #
    # def three_decker(self):
    #     ship_name = 'Cruiser'
    #     ship_length = 3
    #     amount = 2
    #     return ship_name, ship_length, amount
    #
    # def two_decker(self):
    #     ship_name = 'Destroyer'
    #     ship_length = 2
    #     amount = 3
    #     return ship_name, ship_length, amount
    #
    # def single_decker(self):
    #     ship_name = 'Submarine'
    #     ship_length = 1
    #     amount = 4
    #     return ship_name, ship_length, amount


# s1 = Ship(1, 1)
# s2 = Ship(2, 2)
# s3 = Ship(3, 3)
# s4 = Ship(4, 4)
# print(s4.four_decker(), s3.three_decker(), s2.two_decker(), s1.single_decker())
