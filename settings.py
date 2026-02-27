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
        self.human_limit = 3

        #love settings
        self.love_speed = 4
        self.love_width = 15
        self.love_height = 15
        self.love_allowed = 5

        #kitten settings
        self.kitten_width = 78
        self.kitten_height = 50
        self.kitten_speed = 1.0
        self.mattress_drop_speed = 10
        #mattress_direction of 1 represents right; -1 represents left.
        self.mattress_direction = 1