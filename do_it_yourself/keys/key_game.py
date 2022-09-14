import sys

import pygame
from settings_for_key import Settings


class KeyGame:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initiate pygame and setup game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Key Game')

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.update()


if __name__ == '__main__':
    kg = KeyGame()
    kg.run_game()