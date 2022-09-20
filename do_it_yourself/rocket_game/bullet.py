import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A setup for the bullets"""
    def __init__(self, r_game):
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.color = self.settings.bullet_color

        # Implementing the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = r_game.rocket.rect.midtop

        # Store the bullet position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
