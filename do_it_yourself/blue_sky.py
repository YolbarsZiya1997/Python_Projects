import sys
import pygame
from settings_sky import Settings
from game_character import Cowboy


class Sky:
    """Make a game with blue background"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        # set up the window for the game
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky")
        self.cowboy = Cowboy(self)

    def run_game(self):
        """Start a main loop for the game"""
        while True:
            self._check_events()
            self.cowboy.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.cowboy.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.cowboy.move_left = True
                elif event.key == pygame.K_UP:
                    self.cowboy.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.cowboy.move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.cowboy.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.cowboy.move_left = False
                elif event.key == pygame.K_UP:
                    self.cowboy.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.cowboy.move_down = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.cowboy.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    bs = Sky()
    bs.run_game()