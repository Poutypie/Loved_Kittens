class Settings:
    """A class to store all the settings for Loved Kittens."""
    def __init__(self):
        #screen settings:
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (255, 192, 203)
        #human settings:
        self.human_speed = 3.5
        #love settings
        self.love_speed = 4
        self.love_width = 5
        self.love_height = 5
        self.love_color = (255, 100, 150)
        self.love_allowed = 5