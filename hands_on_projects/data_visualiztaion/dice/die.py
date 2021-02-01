from random import randint


class Die():
    '''a class for Dic'''

    def __init__(self, num_sides=6):
        '''a dice has default 6 sides'''
        self.num_sides = num_sides

    def roll(self):
        '''return a number between 1 to number_side'''
        return randint(1, self.num_sides)
