import pygame

# Initialize the pygame
pygame.init()

# Create the screen (width - x, height - y)
screen = pygame.display.set_mode((800,600))

# caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./Pygame/Space_Invader/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./Pygame/Space_Invader/player2.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    #b blit = to draw on screen -> (image, (coordinates))
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # movement in pixel
    #playerY += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #if keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    
    # example: 5 = 5 + 0.1 or -0.1
    playerX += playerX_change

    #boundary of player
    if playerX <=50:
        playerX = 50
    elif playerX >= 700:
        playerX = 700
    
    player(playerX, playerY)
    pygame.display.update()


#27.07