import pygame


class Settings:
    """Make a settings class for easy modification of the game"""
    def __init__(self):
        """basic settings for the game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.rocket_speed = 2.5

        # Bullet settings
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_speed = 1.5
        self.bullet_color = (0, 0, 0)


