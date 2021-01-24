import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # init game and create a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_heigt))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # background color
    bg_color = (ai_settings.bg_color)

    # start game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
