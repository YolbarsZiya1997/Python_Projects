import pygame
import sys
from settings import Settings
from rocket import Rocket


class SpaceShooter:
    """A rocket is lunched into the space to destroy aliens"""

    def __init__(self):
        """Initialize the game and setup game resources"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.rocket = Rocket(self)
        pygame.display.set_caption('Rocket game')

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        elif event.key == pygame.K_UP:
            self.rocket.move_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def _update_screen(self):
        self.screen.fill((123, 222, 231))
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    rg = SpaceShooter()
    rg.run_game()