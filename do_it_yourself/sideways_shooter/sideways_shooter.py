import pygame
import sys
from time import sleep
from random import random
from ss_settings import Settings
from gunman_setup import GunMan
from bullet_setup import Bullet
from ss_game_stats import GameStats
from indian import Indians
from ss_button import Button
from ss_scoreboard import Scoreboard


class SidewaysShooter:
    """Main class for the game"""

    def __init__(self):
        """Initialize the game, and set up game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.make_bullet = False
        self.last_fired_bullet = 0
        self.firing_delay = 100
        # Make the play button.
        self.play_button = Button(self, 'Play')

        # Create an instance to store game statistics,
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.gunman = GunMan(self)
        self.bullets = pygame.sprite.Group()
        self.indians = pygame.sprite.Group()

        pygame.display.set_caption('Sideways Shooter')

    def run_game(self):
        while True:
            self._check_events()
            # Consider creating a new indian
            if self.stats.game_active:
                self._create_horde()
                self._update_indians()
                self.gunman.update()
                if pygame.time.get_ticks() -self.last_fired_bullet >= self.firing_delay:
                    self._make_bullets()
                self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.gunman.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.indians.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.gunman.move_up = True
        elif event.key == pygame.K_DOWN:
            self.gunman.move_down = True
        elif event.key == pygame.K_SPACE:
            self.make_bullet = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.gunman.move_up = False
        elif event.key == pygame.K_DOWN:
            self.gunman.move_down = False
        elif event.key == pygame.K_SPACE:
            self.make_bullet = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_gunmen()

            # Get rid of any remaining aliens and bullets.
            self.indians.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_horde()
            self.gunman.recenter()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _make_bullets(self):
        if self.make_bullet:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.last_fired_bullet = pygame.time.get_ticks()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_indian_collisions()

    def _create_horde(self):
        """Create the hord of indians, if conditions are right."""
        if random() < self.settings.indian_frequency:
            indian = Indians(self)
            self.indians.add(indian)
            print(len(self.indians))

    def _check_bullet_indian_collisions(self):
        """check whether any bullets have hit an alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.indians, True, True
        )
        if collisions:
            for indians in collisions.values():
                self.stats.score += self.settings.indian_points * len(indians)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _update_indians(self):
        self.indians.update()

        # Look for collision between the gunman and the indians
        if pygame.sprite.spritecollideany(self.gunman, self.indians):
            self._man_down()

        # Check for the trespassing indians
        self._check_indian_trespass()

    def _man_down(self):
        """Respond to gunman being hit by an indian"""
        if self.settings.number_of_gunman > 0:
            # Decrement gunmen_left, and update scoreboard.
            self.settings.number_of_gunman -= 1
            self.sb.prep_gunmen()

            # empty the list of indians and bullets
            self.indians.empty()
            self.bullets.empty()

            # make new instances of indians and recenter the ship
            self._update_indians()
            self.gunman.recenter()

            # Pause the game
            sleep(0.7)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_indian_trespass(self):
        """Check if any indians have crossed the right side of the screen"""
        screen_rect = self.screen.get_rect()
        for indian in self.indians.sprites():
            if indian.rect.left <= screen_rect.left:
                self._man_down()
                break


if __name__ == '__main__':
    ss_game = SidewaysShooter()
    ss_game.run_game()
