class Settings():
    ''' a class that stores all settings for alien_invasion game'''

    def __init__(self) -> None:
        '''init all game settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 5
        self.ship_limit = 3

        # bullet seetings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30
        # fleet_direction: 1: right. -1: left
        self.fleet_direction = 1
