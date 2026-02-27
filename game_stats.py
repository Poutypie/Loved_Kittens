class GameStats:
    """track statistics for loved kittens."""
    def __init__(self, lk_game):
        """initialize statistics."""
        self.settings = lk_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.humans_left = self.settings.human_limit