import pygame


class Button:
    """A button class."""
    def __init__(self, tg_game):
        """Initialize the button class."""
        self.screen = tg_game.screen
        self.screen_rect = self.screen.get_rect()

        # Import the button and center it on the screen.
        self.image = pygame.image.load('images/c0921cd2bd146c1.png')
        self.rect = self.image.get_rect()

        # centering the rect onto the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the button on to the screen."""
        self.screen.blit(self.image, self.rect)
