# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *
from parameters.appParams import parameters
import models.Persona
import models.Labyrinth
import models.ItemsList
from utils.filesManagement.get_image_sizing import get_image_sizing
from views.welcomeView import display_welcome_view
from views.gridView import display_grid
from views.endGameView import *

# Labyrinth initialization
level = models.Labyrinth.Labyrinth('resources//maps//map2.txt')

# Windows initialization
sprite_sizing = get_image_sizing('resources//pictures//sprite.png')

pygame.init()
pygame.time.Clock().tick(30)
pygame.display.set_caption('{0} Version: {1}'.format(parameters['gameInfo']['name'], parameters['gameInfo']['version']))
screen = pygame.display.set_mode((len(level.grid)*sprite_sizing[0], (len(level.grid[0])*sprite_sizing[1])))

not_stop = True
display_welcome_page = True
play_level = False
end_game_won = False
end_game_lost = False

while not_stop:
    display_welcome_view(screen)
    while display_welcome_page:
        display_welcome_view(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_stop = False
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                play_level = True
                end_game_won = False
                end_game_lost = False
                display_welcome_page = False

    while end_game_won:
        display_win_view(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_stop = False
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                display_welcome_page = True
                end_game_won = False

    while end_game_lost:
        display_lost_view(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_stop = False
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                display_welcome_page = True
                end_game_lost = False

    if play_level:

        # List of items building up and placing on grid
        items = models.ItemsList.ItemsList()
        items.dispatch_items_randomly(level)

        # Windows initialization
        sprite_sizing = get_image_sizing('resources//pictures//sprite.png')

        # Persona initialization
        player = models.Persona.Persona('player', level.departure, 'Mac Gyver', 'alive', True,
                                        'Resources//pictures//MacGyver.png', items.list)
        enemy = models.Persona.Persona('bad_guy', level.end, 'The Bad Guy', 'bad_guy', False,
                                       'Resources//pictures//Gardien.png', None)
        wall = pygame.image.load('resources//pictures//sprite.png').convert()
        ground = pygame.image.load('resources//pictures//ground2.png').convert()

        display_grid(level, screen, player, wall, ground, pygame.image.load(player.icon).convert(),
                     pygame.image.load(enemy.icon).convert(), sprite_sizing)
        playing = True

        while playing:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    not_stop = False
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                        player.move(event.key, level)
                        player.find_item(level)
                        player.build_sering()
                        player.end_game(level, enemy)
                        display_grid(level, screen, player, wall, ground, pygame.image.load(player.icon).convert(),
                                     pygame.image.load(enemy.icon).convert(), sprite_sizing)
                        if player.status == 'winner' and player.position == enemy.position:
                            end_game_won = True
                            playing = False
                            play_level = False

                        if player.status == 'dead' and player.position == enemy.position:
                            end_game_lost = True
                            playing = False
                            play_level = False

exit()

