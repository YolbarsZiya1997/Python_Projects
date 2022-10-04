import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """The target class for the shooting."""
    def __init__(self, tg_game):
        super().__init__()
        self.screen = tg_game.screen
        self.settings = tg_game.settings

        # target set up
        self.image = pygame.image.load('images/shipsall.png')
        self.rect = self.image.get_rect()

        # set up the location of the target
        self.rect.midright = self.screen.get_rect().midright

        # the exact location
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if target is at the edge of the screen"""
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_rect().bottom:
            return True

    def update(self):
        """Move target up and down."""
        self.y += (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y
