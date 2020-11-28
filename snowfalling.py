import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

myDisplay = pygame.display.set_mode((1110, 600))
pygame.display.set_caption("Snow_Falling")

SonwFlakes = []
for q in range(100):
    x = random.randrange(0, 1110)
    y = random.randrange(0, 590)
    SonwFlakes.append([x, y])
