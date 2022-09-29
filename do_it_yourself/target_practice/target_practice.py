import pygame
import sys
from settings import Settings
from space_ship import SpaceShip
from bullet import Bullet


class TargetPractice:
    """The main file for the target-practice"""
    def __init__(self):
        """Initiate the main file"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.make_bullet = False
        self.last_fired_bullet = 0
        self.firing_delay = 100

        self.space_ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption('Target Practice')

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self.space_ship.update()
            if pygame.time.get_ticks() - self.last_fired_bullet >= self.firing_delay:
                self._make_bullet()
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

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.space_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.space_ship.move_down = True
        elif event.key == pygame.K_UP:
            self.space_ship.move_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.make_bullet = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.space_ship.move_down = False
        elif event.key == pygame.K_UP:
            self.space_ship.move_up = False
        elif event.key == pygame.K_SPACE:
            self.make_bullet = False

    def _make_bullet(self):
        if self.make_bullet:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.last_fired_bullet = pygame.time.get_ticks()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen.get_rect().right:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    tp_game = TargetPractice()
    tp_game.run_game()