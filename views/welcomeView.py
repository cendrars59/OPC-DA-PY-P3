# -*- coding: Utf-8 -*
import pygame


def display_welcome_view(screen):
    """
    function to display the welcome view
    :param screen:
    :return:
    """
    pygame.time.Clock().tick(30)
    welcome_background = pygame.image.load('resources//pictures//startb.jpg').convert()
    screen.blit(welcome_background, (0, 0))
    pygame.display.flip()
