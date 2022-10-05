import pygame


class SpaceShip:
    """The ship class"""
    def __init__(self, tg_game):
        self.screen = tg_game.screen
        self.settings = tg_game.settings

        # set up the image
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # position the ship
        self.rect.midleft = self.screen.get_rect().midleft

        # get the exact coordinate
        self.y = float(self.rect.y)

        # set up the movement flags
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom <= self.screen.get_rect().bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        """center the ship on the midright screen."""
        self.rect.midleft = self.screen.get_rect().midleft
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)