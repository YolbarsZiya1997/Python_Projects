import pygame


class Cowboy:
    """A class to manage the cowboy"""

    def __init__(self, bs_game):
        """Initialize the cowboy and set its starting position"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the cowboy image and get its rectangle
        self.image = pygame.image.load('cb_image/pixilart-drawing.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        # movement flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right:
            self.rect.x += 1
        if self.move_left:
            self.rect.x -= 1
        if self.move_up:
            self.rect.y -= 1
        if self.move_down:
            self.rect.y += 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)