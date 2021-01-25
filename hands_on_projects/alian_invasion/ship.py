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

        # set the ship position related to the screen(container)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery

        # save float number in ship's center attribute
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # movement sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''change the ship's location based on movement sign'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        # if self.moving_left and self.rect.left > 0:
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor

        # update rect obj based on `self.center`
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery

    def blitme(self):
        '''draw a ship in a specific location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''center the ship'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
