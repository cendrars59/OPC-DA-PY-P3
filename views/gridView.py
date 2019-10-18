# -*- coding: Utf-8 -*
import pygame
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)


def display_grid(level, screen, player, wall, ground, playericon, enemyicon, sprite_sizing):
    """
    function to display the grid according the position of each calculated element
    :param level:
    :param screen:
    :param player:
    :param wall:
    :param ground:
    :param playericon:
    :param enemyicon:
    :param sprite_sizing:
    :return:
    """
    row_number = 0
    for row in level.grid:
        col_number = 0
        for column in row:
            x = col_number * sprite_sizing[0]
            y = row_number * sprite_sizing[1]

            if level.grid[row_number][col_number] == 'w':
                screen.blit(wall, (x, y))
            elif level.grid[row_number][col_number] == 's' or level.grid[row_number][col_number] == 'p':
                screen.blit(playericon, (x, y))
            elif level.grid[row_number][col_number] == 'e':
                screen.blit(enemyicon, (x, y))
            elif level.grid[row_number][col_number] == '0':
                screen.blit(ground, (x, y))
            elif level.grid[row_number][col_number] == 'i':
                for item in player.grabbedItems:
                    if item.position == (row_number, col_number):
                        icon = pygame.image.load(item.icon_path).convert()
                        screen.blit(icon, (x, y))
            elif level.grid[row_number][col_number] == 'c':
                if player.type == 'player':
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render(str(player.count_items_found), True, BLUE, GREEN)
                    screen.blit(text, (x, y))
            col_number += 1
        row_number += 1
    pygame.display.flip()
