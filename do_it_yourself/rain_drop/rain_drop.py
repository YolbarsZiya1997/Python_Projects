import pygame
import sys
from settings import Settings


class RainDrop:
    """A class for the rain drops"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption('Rain Drop')

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.update()

    def _check_keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        pass
