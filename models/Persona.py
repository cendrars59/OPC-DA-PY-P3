# -*- coding: Utf-8 -*
from pygame.constants import K_DOWN
from pygame.constants import K_UP
from pygame.constants import K_LEFT
from pygame.constants import K_RIGHT
from utils.filesManagement.import_items import build_list_from_file
from models.Item import Item
from utils.filesManagement.import_maps import build_grid_from_file


class Persona:
    """
    class  in order to create instance of game persona
    caracteristics :
        - position : position on the grid defined by a tuple (row, column)
        - name : name of persona. Type string
        - isGood : define if the persona is a good guy. Type boolean
        - isMoving : define if the persona is allowed to move. Type boolean
        - icon : path to the picture of the persona. Type string
        - grabbedItems : list of items collected by persona. Type list

    methods :
        - persona can move up, down, back, forward.
        - persona gathers items
        - persona can win or lose
    """

    def __init__(self, type, position, name, status, is_allowed_to_move, icon, items_list):
        """
        :param type: Type of the persona. Type string
        :param position: current position of the persona. Type is tuple
        :param name: name of the persona. Type is string
        :param status: Status can the following value 'alive', bad guy', 'dead', 'winner'. Type is string
        :param is_allowed_to_move: persona is allowed to move. Type is boolean
        :param icon: path to the picture to get the persona icon. Type is string
        :param items_list: list of items to retrieve. Type is dictionary
        """

        self.type = type
        self.position = position
        self.name = name
        self.status = status
        self.is_allowed_to_move = is_allowed_to_move
        self.icon = icon
        self.grabbedItems = items_list
        self.has_sering = Item('sering', 'resources//pictures//seringue.png')

    def find_item(self, level):
        """
        function to identify the items found by player along the game.
        :param level: game grid represented by a 2 dimensional array.
        :return:
        """
        if level.grid[self.position[0]][self.position[1]] == 'i':
            for item in self.grabbedItems:
                if item.position == self.position:
                    item.found = True
                    item.icon_path = "{0}_found.png".format(item.name)
                    level.grid[self.position[0]][self.position[1]] = 'f'

    def build_sering(self):
        """
        Function to verify if all items belonging to the list have been found.
        :return:
        """
        if self.status == 'alive':
            found_count = 0
            for item in self.grabbedItems:
                if item.found:
                    found_count += 1

            if found_count == len(self.grabbedItems):
                self.has_sering.found = True
                self.icon = "resources//pictures//pi.png"

    def end_game(self, level, enemy):
        """
        function to define whether the player has lost or won the game.
        :param level:
        :param enemy:
        :return:
        """
        if self.position == level.end and self.has_sering.found and self.status == 'alive' and self.type == 'player':
            self.status = 'winner'
        elif self.position == level.end and not self.has_sering.found and self.status == 'alive' and\
                self.type == 'player':
            self.status = 'dead'

    def move(self, key, level):
        """
        Function to manage the moves of the player according the stroke key.
        User is not allowed to get off the grid or on a wall position. In such case, player stays at the same
        position.

        :param level: game level. Type labyrinth.
        :param key: stroke key. Type string.
        :return:
        """
        next_value_on_grid = 'p'
        # move forward
        if key == K_RIGHT and self.position[1] + 1 <= len(level.grid[0])-1 and\
                level.grid[self.position[0]][self.position[1] + 1] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0], self.position[1] + 1)
            self.position = self.position[0], self.position[1] + 1
            level.grid[self.position[0]][self.position[1]-1] = '0'  # removing the older player position

        # move back
        elif key == K_LEFT and self.position[1] - 1 >= 0 and level.grid[self.position[0]][self.position[1] - 1] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0], self.position[1] - 1)
            self.position = self.position[0], self.position[1] - 1
            level.grid[self.position[0]][self.position[1]+1] = '0'  # removing the older player position

        # move up
        elif key == K_UP and self.position[0] - 1 >= 0 and level.grid[self.position[0] - 1][self.position[1]] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0] - 1, self.position[1])
            self.position = self.position[0] - 1, self.position[1]
            level.grid[self.position[0]+1][self.position[1]] = '0'  # removing the older player position

        # move down
        elif key == K_DOWN and self.position[0] + 1 <= len(level.grid)-1 and\
                level.grid[self.position[0]+1][self.position[1]] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0] + 1, self.position[1])
            self.position = self.position[0] + 1, self.position[1]
            level.grid[self.position[0] - 1][self.position[1]] = '0'  # removing the older player position

        # no move
        else:
            next_value_on_grid = level.find_next_value_on_grid(self.position[0], self.position[1])
            self.position = self.position

        level.grid[self.position[0]][self.position[1]] = next_value_on_grid  # Set new value according new position

    @property
    def count_items_found(self):
        """
        property to get the number of items found by the player
        :return: integer
        """
        items_found_counter = 0
        for item in self.grabbedItems:
            if item.found:
                items_found_counter += 1
        return items_found_counter

