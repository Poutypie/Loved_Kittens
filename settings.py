class Settings:
    """A class to store all the settings for Loved Kittens."""
    def __init__(self):
        #screen settings:
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (255, 192, 203)
        #human settings:
        self.human_speed = 3.5
        self.human_width = 90
        self.human_height = 135
        #love settings
        self.love_speed = 4
        self.love_width = 15
        self.love_height = 15
        #self.love_color = (255, 100, 150)
        self.love_allowed = 5

        #kitten size settings and it's scale
        self.kitten_width = 78
        self.kitten_height = 50