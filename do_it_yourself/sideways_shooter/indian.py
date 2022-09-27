import pygame
from random import randint
from pygame.sprite import Sprite


class Indians(Sprite):
    """A class for the set of indians"""
    def __init__(self, ss_game):
        """Initialize the indians and set its attributes"""
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings

        # Load the alien image and its rect attributes
        self.image = pygame.image.load('images/Indian.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near the top right of the screen
        self.rect.left = self.screen_rect.right
        indian_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(self.rect.height, indian_top_max - self.rect.height)

        # Store the Indian's exact horizontal location
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if indian is at the edge of screen"""
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """Move the indian steadily to the left"""
        self.x -= self.settings.indian_speed
        self.rect.x = self.x
