import sys
import pygame
from shooter_settings import Settings
from character_setup import GunMan


class SidewaysShooter:
    """Main file for the shooter game"""
    def __init__(self):
        """Game resources are here"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Sideways Shooter')
        self.gunman = GunMan(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.gunman.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    side_shoot = SidewaysShooter()
    side_shoot.run_game()