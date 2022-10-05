import pygame


class Settings:
    """The settings class for the target practice game."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (21, 22, 100)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 4
        self.bullet_limit = 3

        # target settings
        self.target_direction = 1

        # overall game dynamics.
        self.miss_limit = 3

        # How quickly the game speeds up.
        self.speedup_scale = 2.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings change throughout the game."""
        self.target_speed = 0.5
        self.bullet_speed = 3.0
        self.ship_speed = 1.5

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale

