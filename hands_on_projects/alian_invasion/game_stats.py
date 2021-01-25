class GameStats():
    '''stats tracking'''

    def __init__(self, ai_settings):
        '''init stats info'''
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        '''reinit all changable data'''
        self.ships_left = self.ai_settings.ship_limit
