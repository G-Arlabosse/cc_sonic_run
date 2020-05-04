import pygame
pygame.init()

screen = pygame.display.set_mode((1200,600))
title = pygame.display.set_caption("SANIK")
background = pygame.image.load("images/bakgraounde.png")
front_ground = pygame.image.load("images/fronte_graounde.png")
SANIK = pygame.image.load("images/sanik.png")

ded= False

while not ded:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(background, [0,0])
    screen.blit(front_ground, [0,450])
    screen.blit(SANIK, [300,380])
    pygame.display.flip()