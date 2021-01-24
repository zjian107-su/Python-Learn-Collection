import pygame


class Ship():

    def __init__(self, ai_settings, screen) -> None:
        '''init a ship and ser its position'''
        self.screen = screen
        self.ai_settings = ai_settings

        # load a ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set the position related to the screen(container)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float number in ship's center attribute
        self.center = float(self.rect.centerx)

        # movement sign
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''change the ship's location based on movement sign'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect obj based on `self.center`
        self.rect.centerx = self.center

    def blitme(self):
        '''draw a ship in a specific location'''
        self.screen.blit(self.image, self.rect)
