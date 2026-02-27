from hmac import new
import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
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

        self.stats = GameStats(self)
        self.human = Human(self)
        self.love = pygame.sprite.Group()
        self.kittens = pygame.sprite.Group()
        self._create_mattress()
        
        #scratch message:
        self.show_scratch_message = False
        self.scratch_time = 0
        self.Smessage_duration = 2000
        self.font = pygame.font.SysFont(None, 36)

        self.game_active = True

    def rungame(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.human.update()
                self.love.update()
                self._update_kittens()
            
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
        self._check_love_kitten_collisions()


    def _check_love_kitten_collisions(self):
        """respond to bullet-kitten collisions."""
        #check for love & kittens collision:
        collisions = pygame.sprite.groupcollide(self.love, self.kittens, 
                                                True, True)
        
        if not self.kittens:
            #destroy existing love bullets and create a new mattress.
            self.love.empty()
            self._create_mattress()

    def _update_kittens(self):
        """update the positions of all kittens in the mattress."""
        self._check_mattress_edges()
        self.kittens.update()

        #look for kitten-human collisions.
        if pygame.sprite.spritecollideany(self.human, self.kittens):
            self._human_scratch()
            self.show_scratch_message = True
            self.scratch_time = pygame.time.get_ticks()
        self._check_kittens_bottom()

    def _create_mattress(self):
        """create the mattress of kittens"""
        #spacing between kittens is one kitten width.
        kitten = Kitten(self)
        kitten_width, kitten_height = kitten.rect.size

        current_x, current_y = kitten_width, kitten_height
        while current_y < (self.settings.screen_height - 3 * kitten_height):
            while current_x < (self.settings.screen_width - 2 * kitten_width):
                self._create_kitten(current_x, current_y)
                current_x += 2 * kitten_width

            #finish a row, reset x value, and increment y value.
            current_x = kitten_width
            current_y += 2 * kitten_height

    def _create_kitten(self, x_position, y_position):
        """create a kitten and place it in the row."""
        new_kitten = Kitten(self)
        new_kitten.x = x_position
        new_kitten.rect.x = x_position
        new_kitten.rect.y = y_position
        self.kittens.add(new_kitten)

    def _check_mattress_edges(self):
        """respond appropriately if any kittens have reached an edge"""
        for kitten in self.kittens.sprites():
            if kitten.check_edges():
                self._change_mattress_directions()
                break

    def _change_mattress_directions(self):
        """drop the entire mattress and change the mattress' direction."""
        for kitten in self.kittens.sprites():
            kitten.rect.y += self.settings.mattress_drop_speed
        self.settings.mattress_direction *= -1

    def _check_kittens_bottom(self):
        """check if any kitten have reached the bottom of the screen."""
        for kitten in self.kittens.sprites():
            if kitten.rect.bottom >= self.settings.screen_height:
                self._human_scratch()
                break

    def _human_scratch(self):
        """respond to the human being scratched by a cat."""
        
        if self.stats.humans_left > 0:
            #decrement human_left.
            self.stats.humans_left -= 1

            #get rid of any remaining love bullets and kittens.
            self.love.empty()
            self.kittens.empty()

            #create a new mattress and center the human.
            self._create_mattress()
            self.human.center_human()

            #pause.
            sleep(0.5)
        else:
            self.game_active = False

    def _scratch_message(self):
        """a class to manage scratch message."""
        
        #showing the scratch message:
        if self.show_scratch_message:
            current_time = pygame.time.get_ticks()
            if current_time - self.scratch_time < self.Smessage_duration:
                #making the text:
                text_scratch = self.font.render(
                    "Kittens just scratched you and ranaway!",
                    True,
                    (0,0,0)
                )
                text_rect = text_scratch.get_rect()
                text_rect.center = self.screen.get_rect().center

                #making the text background:
                padding = 20
                bg_surface = pygame.Surface(
                    (text_rect.width + padding, text_rect.height + padding
                ),
                pygame.SRCALPHA
                )
                bg_surface.fill((255, 255, 255, 180))
                bg_rect = bg_surface.get_rect(center=text_rect.center)

                #draw on the screen:
                self.screen.blit(bg_surface, bg_rect)

                text_rect.center = bg_rect.center
                self.screen.blit(text_scratch, text_rect)
            else:
                self.show_scratch_message = False

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for spark in self.love.sprites():
            spark.draw_love()
        self.human.blitme()
        self.kittens.draw(self.screen)
        self._scratch_message()

        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game.
    lk = LovedKittens()
    lk.rungame()