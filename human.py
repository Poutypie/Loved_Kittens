import pygame

class Human:
    """to manage the little cute humans the users choose to be."""
    def __init__(self, lk_game):
        """initialize the humans and set their starting position."""
        self.screen = lk_game.screen
        self.settings = lk_game.settings
        self.screen_rect = lk_game.screen.get_rect()

        #loading the human image:
        self.image = pygame.image.load('assets/images/humans/IMG_Human_1.bmp')

        #scale the image to a smaller size
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.human_width, self.settings.human_height)
        )

        self.rect = self.image.get_rect()

        #start each new human at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the human's exact horizontal position.
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the human's positon based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.human_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.human_speed
        #update rect object from self.x.
        self.rect.x = self.x
        
    def blitme(self):
        """draw the human at its current location."""
        self.screen.blit(self.image,self.rect)  

    def center_human(self):
        """center the human on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)