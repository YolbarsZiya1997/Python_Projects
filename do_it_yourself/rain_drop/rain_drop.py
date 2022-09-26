import pygame
import sys
from settings import Settings
from droplets import Droplets


class RainDrop:
    """A class for the rain drops"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.droplets = pygame.sprite.Group()
        pygame.display.set_caption('Rain Drop')
        self._create_droplets()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrop()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.droplets.draw(self.screen)
        pygame.display.update()

    @staticmethod
    def _check_keydown_event(event):
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        pass

    def _create_droplets(self):
        """Create the row of raindrops"""
        # Make a rain drop
        droplet = Droplets(self)
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        droplet_width, droplet_height = droplet.rect.size
        available_space_x = self.settings.screen_width - droplet_width
        self.num_of_droplets = available_space_x // (1 * droplet_width)

        # Determine the number of rows of aliens that fit on the screen.
        available_space_y = self.settings.screen_height - 300
        number_rows = available_space_y // droplet_height
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """Create a single row of raindrops."""
        for droplet_number in range(self.num_of_droplets):
            self._create_raindrops(droplet_number, row_number)

    def _create_raindrops(self, droplet_number, row_number):
        # Create a droplet and place it in the row
        droplet = Droplets(self)
        droplet_width, droplet_height = droplet.rect.size
        droplet.x = droplet_width + 1 * droplet_width * droplet_number
        droplet.rect.x = droplet.x
        droplet.y = droplet.rect.height * row_number
        droplet.rect.y = droplet.y
        self.droplets.add(droplet)

    def _update_raindrop(self):
        """Update teh positions of all aliens in the fleet"""
        self.droplets.update()

        # Assume we won't make new drops.
        make_new_drops = False
        for drop in self.droplets.copy():
            if drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops
                self.droplets.remove(drop)
                make_new_drops = True

        # Nake a new row of drops if needed
        if make_new_drops:
            self._create_row(0)


if __name__ == '__main__':
    rain_drop = RainDrop()
    rain_drop.run_game()