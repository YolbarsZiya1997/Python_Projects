import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """The bullet class."""
    def __init__(self, tg_game):
        super().__init__()

        self.screen = tg_game.screen
        self.settings = tg_game.settings
        self.color = tg_game.settings.bullet_color

        # Create the bullet at (0, 0) and then move the rect to the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = tg_game.ship.rect.midright

        # set up the exact location
        self.x = float(self.rect.x)

    def update(self):
        """Update bullets position on the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet onto the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)