import pygame
from pygame.sprite import Sprite


class Droplets(Sprite):
    """Import the image and set up the attributes"""

    def __init__(self, rd_sim):
        """Initiate the alien and set its starting position"""
        super().__init__()
        self.screen = rd_sim.screen
        self.settings = rd_sim.settings

        # Load the alien image and set its rect attributes
        self.image = pygame.image.load('images/pixil-frame-0_1_.bmp')
        self.rect = self.image.get_rect()

        # Start each new droplets near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the alien right."""
        self.y += self.settings.alien_speed
        self.rect.y = self.y