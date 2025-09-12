import pygame
from pygame.sprite import Sprite

class Love(Sprite):
    """a class to manage loves that users throw."""

    def __init__(self, lk_game):
        """create a love object at the human's current poition"""
        super().__init__()
        self.screen = lk_game.screen
        self.settings = lk_game.settings
        self.color = self.settings.love_color

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.love_width,
                                 self.settings.love_height)
        self.rect.midtop = lk_game.human.rect.midtop

        #store the love's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """update the decimal position of the love we shoot."""
        self.y -= self.settings.love_speed
        #update the rect  position.
        self.rect.y = self.y

    def draw_love(self):
        """draw the love bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
