import pygame.font
from pygame.sprite import Group
from gunman_setup import GunMan


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ss_game):
        """Initialize score keeping attributes."""
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('loma', 30)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_gunmen()

    def prep_score(self):
        """Turn the score into a rendered image."""
        round_score = round(self.stats.score, -1)
        score_str = f"Score: {round_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_gunmen(self):
        """Show how many ships are left."""
        self.gunmen = Group()
        for gunman_number in range(self.stats.gunman_left):
            gunman = GunMan(self.ss_game)
            gunman.rect.x = 10 + gunman_number * gunman.rect.width
            gunman.rect.y = 10
            self.gunmen.add(gunman)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.gunmen.draw(self.screen)