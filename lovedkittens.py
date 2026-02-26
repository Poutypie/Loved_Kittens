from hmac import new
import sys
import pygame
from settings import Settings
from human import Human
from love import Love
from kitten import Kitten


class LovedKittens:
    """overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.clock =pygame.time.Clock()
        self.settings = Settings()

        #automating the size of screen:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Loved Kittens")
        self.human = Human(self)
        self.love = pygame.sprite.Group()
        self.kittens = pygame.sprite.Group()

        self._create_mattress()

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

    def _create_mattress(self):
        """create the mattress of kittens"""
        #spacing between kittens is one kitten width.
        kitten = Kitten(self)
        kitten_width = kitten.rect.width
        kitten_height = kitten.rect.height

        current_x = self.settings.kitten_width
        while current_x < (self.settings.screen_width - 2 * kitten_width):
            self._create_kitten(current_x)
            current_x += 2 * kitten_width

    def _create_kitten(self, x_position):
        """create a kitten and place it in the row."""
        new_kitten = Kitten(self)
        new_kitten.x = x_position
        new_kitten.rect.x = x_position
        self.kittens.add(new_kitten)


    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for spark in self.love.sprites():
            spark.draw_love()
        self.human.blitme()
        self.kittens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game.
    lk = LovedKittens()
    lk.rungame()