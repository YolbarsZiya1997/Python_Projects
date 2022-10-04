import pygame


class Settings:
    """The settings class for the target practice game."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (21, 22, 100)

        # ship settings
        self.ship_speed = 1.7

        # bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 1.7
        self.bullet_allowed = 4

        # target settings
        self.target_speed = 0.5
        self.target_direction = 1

