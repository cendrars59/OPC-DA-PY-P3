# -*- coding: Utf-8 -*
import pygame


def display_grid(level, screen, player, wall, ground, playericon, enemyicon, sprite_sizing):
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

            col_number += 1
        row_number += 1
    pygame.display.flip()
