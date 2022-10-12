import pygame


class Settings:
    """The settings class for the sideways shooter game"""
    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 20, 10)

        # Gunman settings
        self.number_of_gunman = 4
        self.movement_speed = 1.7

        # Indian settings
        # indian_frequency controls how often a new indian appears.
        # Higher value -> more frequent aliens. Max = 1.0
        self.indian_frequency = 0.008
        self.indian_speed = 0.2

        # set up the bullet color
        self.bullet_allowed = 20
        self.bullet_width = 15
        self.bullet_height = 7
        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 2.5

        # Scoring
        self.indian_points = 10
