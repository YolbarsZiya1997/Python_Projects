import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to set up the bullets"""
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color

        # Set up the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = tp_game.space_ship.rect.midright

        # get the correct coordinate of the bullet
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right side of the screen"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

