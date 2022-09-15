import pygame


class Settings:
    """The settings class for the sideways shooter game"""
    def __init__(self):
        """Main settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 20, 10)

        # moving speed
        self.movement_speed = 1.7

        # set up the bullet color
        self.bullet_allowed = 6
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 1.7
