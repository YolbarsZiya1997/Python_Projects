import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a fleet of aliens"""

    def __init__(self, r_game):
        super().__init__()
        self.screen = r_game.screen

        # load the image on to the screen
        self.image = pygame.image.load('images/shipsall(1).bmp')
        self.rect = self.image.get_rect()

        # Printing it on the left top corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the coordinates of the alien in decimals
        self.x = float(self.rect.x)