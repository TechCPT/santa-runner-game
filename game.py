import pygame
from pygame import mixer
import sys
import math
import random

# Initializes Pygame
pygame.init ()

# Screen Size
screen = pygame.display.set_mode ((1000,650))

# Sets name of tab
pygame.display.set_caption("Santa Saves Christmas")

# Player
playerImg = pygame.image.load('./images/player_2/player_stand1.png')
playerX = 25
playerY = 430
playerX_change = 0
playerY_change = 0

def player () :
    screen.blit (playerImg, (playerX, playerY))


# Creates Game Loop
running = True
while running :
    screen.fill ((0, 0, 0))
    player ()

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            pygame.quit(); sys.exit()
            running == False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerX_change = -1
            if event.key == pygame.K_RIGHT :
                playerX_change = 1
            if event.key == pygame.K_UP :
                for event in pygame.event.get () :
                    i = 0
                    while i < 2 :
                        playerY_change = 1
                        i += 1
                        playerY += playerY_change
                    while i > 0 :
                        playerY_change = -1
                        i -= 1
                        playerY += playerY_change

        if event.type == pygame.KEYUP :
                playerX_change = 0


    playerX += playerX_change

    pygame.display.update ()
