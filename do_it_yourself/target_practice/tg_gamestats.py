class GameStats:
    """Track statistics for the Target practice."""

    def __init__(self, tg_game):
        """Initiate statistics."""
        self.settings = tg_game.settings
        # start alien invasion in an active state.
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.num_misses = 0