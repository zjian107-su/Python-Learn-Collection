import sys
import pygame


def check_keydown_events(event, ship):
    '''respond to keydown'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        print('keyDownRIght')
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
        print('keyDownLeft')


def check_keyup_events(event, ship):
    '''respond to keyup'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        print('keyUpRIght')
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        print('keyUpLeft')


def check_events(ship):
    """check mouse and keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    '''update images on display and switch to new screen'''
    # redraw in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # only the newest screen can be visible
    pygame.display.flip()
