class Settings():
    ''' a class that stores all settings for alien_invasion game'''

    def __init__(self) -> None:
        '''init all game settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet seetings
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # alien settings
        self.fleet_drop_speed = 30

        # speedup settings
        self.speedup_scale = 1.1
        # aline score speedup settings
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''init changes when game evolves'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction: 1: right. -1: left
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        '''increase speed setting'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
