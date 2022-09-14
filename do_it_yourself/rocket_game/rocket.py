import pygame


class Rocket:
    """A class to manage the cowboy"""

    def __init__(self, rg_game):
        """Initialize the cowboy and set its starting position"""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        # Load the cowboy image and get its rectangle
        self.image = pygame.image.load('images/pixilart-drawing.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center

        # store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.move_left and self.rect.left > 0:
            self.x -= 1
        if self.move_up and self.rect.top > 0:
            self.y -= 1
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        # update the rect
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
