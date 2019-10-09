# -*- coding: Utf-8 -*
from random import randint


class Item:

    def __init__(self, name, icon_path):
        """
        Function to create an item
        :param name: Name of the item. Type string.
        :param icon_path: Path of the picture of the item. Type string.
        """
        self.name = name
        self.position = None
        self.icon_path = icon_path
        self.found = False

    def define_random_position(self, level):
        """
        defining a random position for an item.Position type is tuple
        :param level: labyrinth
        :return:self.position
        """
        position_found = False
        while not position_found:
            row = randint(1, len(level.grid)-1)
            column = randint(1, len(level.grid[0])-1)
            if level.grid[row][column] != 'w':
                self.position = (row, column)
                level.grid[row][column] = 'i'
                position_found = True
        return self.position





