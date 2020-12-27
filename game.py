import pygame

# Initializes Pygame
pygame.init ()

# Screen Size
screen = pygame.display.set_mode ((1000,650))

# Sets name of tab
pygame.display.set_caption("Santa Saves Christmas")

# Player
playerImg = pygame.image.load('standingSanta.png')
playerX = 25
playerY = 440
playerX_change = 0
playerY_change = 0

bg = pygame.image.load('full.png')

def player () :
    screen.blit (playerImg, (playerX, playerY))


# Creates Game Loop
running = True
while running :

    screen.blit (bg, (0, 0))

    player ()

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            pygame.quit(); sys.exit()
            running == False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerX_change = -5
            if event.key == pygame.K_RIGHT :
                playerX_change = 5
            if event.key == pygame.K_UP :
                playerY_change = -6
        if event.type == pygame.KEYUP :
            playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 300:
        playerY_change = 6
    elif playerY >= 440 :
        playerY = 440
        playerY_change = 0
    playerY += playerY_change

    pygame.display.update ()
