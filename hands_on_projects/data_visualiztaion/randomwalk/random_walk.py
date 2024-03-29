from random import choice


class RandomWalk():
    '''generate a class that walks data randomly'''

    def __init__(self, num_points=5000):
        '''init random walk attrubute'''
        self.num_points = num_points

        # all walk start on (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all points in random walks'''

        # walk until reach the length of the list
        while len(self.x_values) < self.num_points:

            # # decide direction and distance
            # x_direction = choice([1, -1])
            # # x_distance = choice([0, 1, 2, 3, 4])
            # x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 30])
            x_step = self.get_step()

            # y_direction = choice([1, -1])
            # # y_distance = choice([0, 1, 2, 3, 4])
            # y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 30])
            y_step = self.get_step()

            # if didnt move, it does not count
            if x_step == 0 and y_step == 0:
                continue

            # calculate next x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 30])
        step = direction * distance
        return step
