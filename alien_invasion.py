import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)



    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(120)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.ship.moving_left = False



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


