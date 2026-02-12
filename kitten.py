import pygame
from pygame.sprite import Sprite
from settings import Settings

class Kitten(Sprite):
    """a class to represent a single kitten in the mattress."""
    
    def __init__(self, lk_game):
        super().__init__()
        self.screen = lk_game.screen
        self.settings = lk_game.settings

        #loading the kitten image and its rect attribute.
        self.image = pygame.image.load('assets/images/kittens/normal_kitten_0.bmp')
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.kitten_width, self.settings.kitten_height)
        )
        self.rect = self.image.get_rect()

        #scale the image to a smaller size
        self.image = pygame.transform.scale(self.image, 
                    (self.settings.kitten_width, self.settings.kitten_height))

        #start each new kitten near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing the kitten's exact horizontal position.
        self.x = float(self.rect.x)