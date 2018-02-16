#!/usr/bin/env python3

class Ship:



    def __init__(self):
        #self.id = Ship.ship_id()
        #Ship.ship_id += 1
        #ship_id = id(self)
        pass

    def __del__(self):
        pass

    def four_decker(self):
        ship_name = 'Battleship'
        ship_length = 4
        amount = 1
        return ship_name, ship_length, amount

    def three_decker(self):
        ship_name = 'Cruiser'
        ship_length = 3
        amount = 2
        return ship_name, ship_length, amount

    def two_decker(self):
        ship_name = 'Destroyer'
        ship_length = 2
        amount = 3
        return ship_name, ship_length, amount

    def single_decker(self):
        ship_name = 'Submarine'
        ship_length = 1
        amount = 4
        return ship_name, ship_length, amount


s1 = Ship()
s2 = Ship()
s3 = Ship()
s4 = Ship()
print(s4.four_decker(), s3.three_decker(), s2.two_decker(), s1.single_decker())
