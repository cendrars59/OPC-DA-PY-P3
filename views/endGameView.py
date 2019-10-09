import pygame


def display_win_view(screen):
    """
    function to display the success screen
    :param screen:
    :return:
    """

    pygame.time.Clock().tick(30)
    screen.blit(pygame.image.load('resources//pictures//winb.jpg').convert(), (0, 0))
    pygame.display.flip()


def display_lost_view(screen):
    """
    function to display the game over screen
    :param screen:
    :return:
    """
    pygame.time.Clock().tick(30)
    screen.blit(pygame.image.load('resources//pictures//lostb.jpg').convert(), (0, 0))
    pygame.display.flip()