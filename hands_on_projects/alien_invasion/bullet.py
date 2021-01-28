import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''a class that manages a ship's bullets'''

    def __init__(self, ai_settings, screen, ship):
        '''create a bullet object at the ship's position'''
        super().__init__()
        self.screen = screen

        # create a rect at (0, 0), then set right position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # use float numver to rep a bullet's potion
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
      '''move up'''
      # update bullet position
      self.y -= self.speed_factor
      # update bullet rect position
      self.rect.y = self.y

    def draw_bullet(self):
      '''draw bullets on a screen'''
      pygame.draw.rect(self.screen, self.color, self.rect)
      

