import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''respond to keydown'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # create a bullet and add it into bullets Group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    '''if haven not reached to the limit, fire a bullet'''
    if len(bullets) < ai_settings.bullets_allowed:  # bullet num limit
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    '''respond to keyup'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """check mouse and keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    '''start game when Play button is clicked'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        ai_settings.initialize_dynamic_settings()

        # reset game stats info
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # reset scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # empty aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new group of aliens and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''update images on display and switch to new screen'''
    # redraw in every loop
    screen.fill(ai_settings.bg_color)
    # draw bullets after ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # show score
    sb.show_score()

    # if the game is inactive, draw Play button
    if not stats.game_active:
        play_button.draw_button()

    # only the newest screen can be visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''update bullet position, and remove disapeared bullets'''
    # update bullet position
    bullets.update()

    # remove disapared bullet and print sprite number
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(bullets) # for testing bullet delete function

    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''respond to the collision of an alien and a bullet'''

    # remove collided alien and bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:
        # remove all bullets and renew a group of aliens
        bullets.empty()
        ai_settings.increase_speed()

        # increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    '''calculate how many alines in a line'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''calculate how many lines of aliens'''
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''create an alien and position it in the current line'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    ''' create an alien fleet'''
    # create an lien and calculate how many in a line
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        # create the first line of aliens
        for alien_number in range(number_aliens_x):
            # create one alien and add it in the line
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''react when one alien touches the edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''move all aliens down and change their direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    check if there are aliens touching the edge
        then update positions for all aliens
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # detect a collision between an alien and a ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # check if an alien touches the bottom edge
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''check if an alien touches the bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # act like ship collision
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''the ship responds when collides with an alien'''

    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

        # empty the alien list and the bullet list
        aliens.empty()
        bullets.empty()

        # create a new group of aliens and re-position the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # palse
        sleep(2)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    '''check if new high score'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
