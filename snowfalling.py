import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

myDisplay = pygame.display.set_mode((1110, 600))
pygame.display.set_caption("Snow_Falling")

SnowFlakes = []
for q in range(100):
    x = random.randrange(0, 1110)
    y = random.randrange(0, 590)
    SnowFlakes.append([x, y])

clock = pygame.time.Clock()
snow = False
background_position = [0, 0]
background_image=pygame.image.load("Background.jpeg").convert()

while not snow:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snow = True

    myDisplay.blit(background_image,background_position)


