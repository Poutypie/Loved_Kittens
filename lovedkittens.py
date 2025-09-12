import sys
import pygame
from settings import Settings
from human import Human
from love import Love

class LovedKittens:
    """overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.clock =pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #self.screen = pygame.display.set_mode(
            #(self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Loved Kittens")
        self.human = Human(self)
        self.love = pygame.sprite.Group()

    def rungame(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            self.human.update()
            self.love.update()
            self._update_screen()
            self._update_love()
            pygame.display.flip()
            self.clock.tick(60)


    def _check_events(self):
        """respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.human.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.human.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_love()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.human.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.human.moving_left = False

    def _fire_love(self):
        """create a new love bullet and add  it to the bullets group."""
        if len(self.love) < self.settings.love_allowed:
            new_love = Love(self)
            self.love.add(new_love)

    def _update_love(self):
        #update bullet positions.
        self.love.update()
        #get rid of disappeared love bullets.
        for lv in self.love.copy():
            if lv.rect.bottom <=0:
                self.love.remove(lv)

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for spark in self.love.sprites():
            spark.draw_love()
        self.human.blitme()

if __name__ == '__main__':
    #make a game instance, and run the game.
    lk = LovedKittens()
    lk.rungame()