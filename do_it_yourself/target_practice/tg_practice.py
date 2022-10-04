import pygame
import sys
from tg_settings import Settings
from tg_ship import SpaceShip
from tg_bullet import Bullets
from tg_target import Target


class TargetPractice:
    """the main class for the target practice game."""
    def  __init__(self):
        """the main function for the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()

        self._create_targets()
        pygame.display.set_caption('Target Practice')

    def run_game(self):
        while True:
            self._check_events()
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

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.targets.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    tg_game = TargetPractice()
    tg_game.run_game()
