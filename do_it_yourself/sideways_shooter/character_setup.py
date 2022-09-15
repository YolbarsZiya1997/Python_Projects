import pygame


class GunMan:
    """This is the game character setup"""

    def __init__(self, ss_game):
        """Setting up the attributes"""
        self.screen = ss_game
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # set up the character by importing the image
        self.image = pygame.image.load('images/pixil-frame-0.bmp')
        self.rect = self.image.get_rect()

        # start each new gunman at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)