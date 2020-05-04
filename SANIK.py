import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1200,600))
title = pygame.display.set_caption("SANIK")

background = pygame.image.load("images/bakgraounde.png")
front_ground = pygame.image.load("images/fronte_graounde.png")
SANIK = pygame.image.load("images/sanik.png")

coordBG1=[0,0]
coordFG1=[0,455]
coordBG2=[1200,0]
coordFG2=[1200,455]
coordSANIK=[500,350]

ded= False

while not ded:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_LEFT:
                coordBG1[0]+=30
                coordBG2[0]+=30
                coordFG1[0]+=30
                coordFG2[0]+=30
            if event.key == pygame.locals.K_RIGHT:
                coordBG1[0]-=30
                coordBG2[0]-=30
                coordFG1[0]-=30
                coordFG2[0]-=30
    if coordBG1[0]<=-1200:
        coordBG1[0]=1200
    if coordBG2[0]<=-1200:
        coordBG2[0]=1200
    if coordFG1[0]<=-1200:
        coordFG1[0]=1200
    if coordFG2[0]<=-1200:
        coordFG2[0]=1200

    # Set numéro 1
    screen.blit(background, coordBG1)
    screen.blit(front_ground, coordFG1)
    # Set numéro 2
    screen.blit(background, coordBG2)
    screen.blit(front_ground, coordFG2)
    screen.blit(SANIK, coordSANIK)
    pygame.display.flip()