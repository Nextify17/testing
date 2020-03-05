import pygame
class Settings():
    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        screen = pygame.display.set_mode((1200, 800))
        self.bg_color = pygame.image.load("images/space.png").convert()
        #self.bg_color = (0, 0, 0)
        self.ship_speed_factor = 1.5
        #Bullets settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 10, 255, 0
        self.bullets_allowed = 5
        #Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1
        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #How fast the game speeds up
        self.speedup_scale = 1.05
        self.initialize_dynamic_settings()
        #alien point value
        self.score_scale = 1.5
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
