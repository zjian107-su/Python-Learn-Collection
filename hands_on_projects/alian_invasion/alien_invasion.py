import sys
import pygame


class Settings():
    ''' a class that stores all settings for alien_invasion game'''

    def __init__(self) -> None:
        '''init all game settings'''
        self.screen_width = 1200
        self.screen_heigt = 800
        self.bg_color = (230, 230, 230)


def run_game():
    # init game and create a screen obj
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_heigt))
    pygame.display.set_caption("Alien Invasion")

    # background color
    bg_color = (ai_setting.bg_color)

    # start game loop
    while True:

        # monitor mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # re-paint the screen in every loop
        screen.fill(ai_setting.bg_color)

        # only the newest screen can be visible
        pygame.display.flip()


run_game()
print('it works')
