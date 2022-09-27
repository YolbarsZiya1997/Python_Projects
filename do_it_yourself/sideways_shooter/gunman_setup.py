import pygame


class GunMan:
    """Basic setup for the gunman class"""
    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('images/pixil-frame-0.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        # start a decimal value for the gunman's vertical position
        self.y = float(self.rect.y)

        # Movement flags
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.movement_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.movement_speed

        # Update the rect object from self.x
        self.rect.y = self.y

    def recenter(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
