import pygame


class Settings:
    """Set up the settings for the target practice."""
    def __init__(self):
        """Initiate the class"""
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (201, 221, 109)

        # ship settings
        self.ship_speed = 1.8

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 1.7


