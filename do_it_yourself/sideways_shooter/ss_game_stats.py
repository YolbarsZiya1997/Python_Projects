class GameStats:
    """The class for the statistics of the game"""

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.gunman_left = self.settings.number_of_gunman