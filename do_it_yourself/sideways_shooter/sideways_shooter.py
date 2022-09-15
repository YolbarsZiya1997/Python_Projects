import pygame
import sys
from ss_settings import Settings
from gunman_setup import GunMan
from bullet_setup import Bullet


class SidewaysShooter:
    """Main class for the game"""
    def __init__(self):
        """Initialize the game, and set up game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.gunman = GunMan(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption('Sideways Shooter')

    def run_game(self):
        while True:
            self._check_events()
            self.gunman.update()
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
        self.gunman.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.gunman.move_up = True
        elif event.key == pygame.K_DOWN:
            self.gunman.move_down = True
        elif event.key == pygame.K_SPACE:
            self.__fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.gunman.move_up = False
        elif event.key == pygame.K_DOWN:
            self.gunman.move_down = False

    def __fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        print(len(self.bullets))


if __name__ == '__main__':
    ss_game = SidewaysShooter()
    ss_game.run_game()
