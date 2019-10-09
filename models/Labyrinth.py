# -*- coding: Utf-8 -*
from utils.filesManagement.import_maps import build_grid_from_file


class Labyrinth:
    """
    Class to manage the grid of the game according a provided map file.
    The grid is represented by 2 dimensional array.


    methods :
        - generating the grid according an input file.
        - defining the departure position
        - defining end position
        - defining the positions of the items to grab
        - getting the detailed items list.
    """

    def __init__(self, file):
        """
        initialization function in order to generate the game grid from a map file
        :param file: input txt file in order to generate the game grid
        """
        self.grid = build_grid_from_file(file)

    @property
    def departure(self):
        """
        retrieve the departure position on the grid. Departure is define by the value d into the map
        file.
        :return: the departure position. Type is a tuple
        """
        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 's':
                    return index_row, index_column
                index_column += 1
            index_row += 1

    @property
    def end(self):
        """
        retrieve the end position on the grid. Departure is define by the value f into the map
        file.
        :return: the departure position. Type is a tuple
        """
        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 'e':
                    return index_row, index_column
                index_column += 1
            index_row += 1

    def find_next_value_on_grid(self, next_row, next_column):
        """
        function to calculate the next value on the grid according the move of the player
        :param next_row: calculated next row number according the player's move .Type int.
        :param next_column: calculated next row number according the player's move .Type int.
        :return: value of Type string
        """
        if self.grid[next_row][next_column] == '0':
            return 'p'
        elif self.grid[next_row][next_column] == 'i':
            return 'i'
        elif self.grid[next_row][next_column] == 'f':
            return 'f'
        elif self.grid[next_row][next_column] == 'e':
            return 'e'
        elif self.grid[next_row][next_column] == 'p':
            return 'p'






