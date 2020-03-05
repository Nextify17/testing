import pygame
from pygame.sprite import Group 
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from music import Music
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    play_button = Button(ai_settings, screen, "Play")
    pygame.display.set_caption("Space Invaders")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    background_image = pygame.image.load("images/space.png").convert()
    Music()
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        screen.blit(background_image, [0, 0])
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))

run_game()

#left on page 308 (76) of the pdf instructions

