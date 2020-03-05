import pygame
from random import randrange
def Music():
    musChoose = randrange(0, 2)
    if musChoose == 0:
        pygame.mixer.music.load("music/butterfly.wav")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("music/XYZ.wav")
        pygame.mixer.music.play(-1)
