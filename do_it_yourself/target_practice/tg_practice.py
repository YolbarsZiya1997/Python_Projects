import pygame
import sys
from tg_settings import Settings
from tg_ship import SpaceShip
from tg_bullet import Bullets
from time import sleep
from tg_gamestats import GameStats
from tg_target import Target
from tg_button import Button


class TargetPractice:
    """the main class for the target practice game."""
    def  __init__(self):
        """the main function for the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.stats = GameStats(self)
        self.ship = SpaceShip(self)
        self.button = Button(self)
        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()

        self._create_targets()
        pygame.display.set_caption('Target Practice')

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_targets()
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

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play."""
        # reset the game statistics.
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining targets and bullets.
            self.targets.empty()
            self.bullets.empty()

            # Create a new target and center the ship.
            self._create_targets()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullet_allowed:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._increment_misses()

        self._check_bullet_target_collisions()

    def _increment_misses(self):
        """Increment the number of misses and check if the game should end."""
        self.stats.num_misses += 1
        self._target_missed()

    def _check_bullet_target_collisions(self):
        # Check for any bullets that have hit targets.
        # If so, get rid of the bullets and the target
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.targets, True, True
        )

        if not self.targets:
            # Create new target.
            self._create_targets()

    def _create_targets(self):
        """Create a target"""
        new_target = Target(self)
        self.targets.add(new_target)

    def _update_targets(self):
        """Update the position of all aliens in the fleet."""
        self._check_target_edges()
        self.targets.update()

    def _check_target_edges(self):
        """Respond appropriately if any target reached an edge."""
        for target in self.targets.sprites():
            if target.check_edges():
                self._change_target_direction()
                break

    def _change_target_direction(self):
        """Drop the target and change the target's direction."""
        for target in self.targets.sprites():
            self.settings.target_direction *= -1

    def _target_missed(self):
        """Respond to the target being missed."""
        # Decrement bullets left.
        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1

            # Get rid of any remaining targets and bullets.
            self.targets.empty()
            self.bullets.empty()

            # Create a new target and center the ship.
            self._create_targets()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.targets.draw(self.screen)
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.button.blitme()
        pygame.display.update()


if __name__ == '__main__':
    tg_game = TargetPractice()
    tg_game.run_game()
