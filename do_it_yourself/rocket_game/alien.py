import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a fleet of aliens"""

    def __init__(self, r_game):
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings

        # load the image on to the screen
        self.image = pygame.image.load('images/shipsall(1).bmp')
        self.rect = self.image.get_rect()

        # Printing it on the left top corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the coordinates of the alien in decimals
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
