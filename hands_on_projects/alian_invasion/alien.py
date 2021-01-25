import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''a class that represents a single alient'''

    def __init__(self, ai_settings, screen) -> None:
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set up the rect attribution
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alian should be located at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # load accurate alien location
        self.x = float(self.rect.x)

    def blitme(self):
        '''draw an alien in a specific location'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move alien to the right'''
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''returns true if an alien touches the edge'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    
