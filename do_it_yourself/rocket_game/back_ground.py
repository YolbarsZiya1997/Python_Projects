import pygame
from settings import Settings


class BackGround:
    def __init__(self):
        """Make a moving background"""
        pygame.init()
        self.screen = pygame.display.set_mode(
            (1200, 800)
        )
        self.settings = Settings()
        self.bg_image = pygame.transform.scale(
            self.settings.bg_image, (self.settings.screen_width, self.settings.screen_height)
        )

    def updater(self):
        i = 0
        while True:
            self.screen.blit(self.bg_image, (0, i))
            self.screen.blit(self.bg_image, (0, -self.settings.screen_height + i))
            # the minus sign here indicates that the image are coming from above the window
            # if we gave it +, the image would already be below the window
            if i == self.settings.screen_height:
                self.screen.blit(self.bg_image, (0, -self.settings.screen_height + i))
                i = 0
            i += 1
            pygame.display.update()


if __name__ == '__main__':
    rg = BackGround()
    rg.updater()