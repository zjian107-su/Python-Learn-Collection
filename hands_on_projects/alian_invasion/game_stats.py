class GameStats():
    '''stats tracking'''

    def __init__(self, ai_settings):
        '''init stats info'''
        self.high_score = 0
        self.ai_settings = ai_settings
        self.reset_stats()

        # defualt as inactive
        self.game_active = False

    def reset_stats(self):
        '''reinit all changable data'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
