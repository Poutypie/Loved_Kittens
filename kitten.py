import pygame
from pygame.sprite import Sprite

class Kitten(Sprite):
    """a class to represent a single kitten in the mattress."""
    
    def __init__(self, lk_game):
        super().__init__()
        self.screen = lk_game.screen
