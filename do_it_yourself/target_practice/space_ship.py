import pygame


class SpaceShip:
    """set up the spaceship class"""
    def __init__(self, tp_game):
        self.screen = tp_game.screen
        self.settings = tp_game.settings

        # Load the image for the ship
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # Positioning the ship on the screen
        self.rect.midleft = self.screen.get_rect().midleft

        # Setting up the movement flags
        self.move_up = False
        self.move_down = False

        # Get the exact coordination of the ship
        self.y = float(self.rect.y)

    def update(self):
        if self.move_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom <= self.screen.get_rect().bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        # Draw the ship on to the screen
        self.screen.blit(self.image, self.rect)