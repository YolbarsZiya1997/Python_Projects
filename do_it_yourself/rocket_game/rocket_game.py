import pygame
import sys
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from random import randint


class SpaceShooter:
    """A rocket is lunched into the space to destroy aliens"""

    def __init__(self):
        """Initialize the game and setup game resources"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption('Rocket game')

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        elif event.key == pygame.K_UP:
            self.rocket.move_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def _update_screen(self):
        self.screen.fill((123, 222, 231))
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        alien_number_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        rocket_height = self.rocket.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - 2 * rocket_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(alien_number_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number

        # Randomize the position of the stars
        alien.rect.x += randint(-200, 200)
        alien.rect.y += randint(-200, 200)
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    rg = SpaceShooter()
    rg.run_game()