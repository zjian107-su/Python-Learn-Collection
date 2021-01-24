class Settings():
    ''' a class that stores all settings for alien_invasion game'''

    def __init__(self) -> None:
        '''init all game settings'''
        self.screen_width = 1200
        self.screen_heigt = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (135, 206, 235) can mk

        # setting for the ship
        self.ship_speed_factor = 1.5
