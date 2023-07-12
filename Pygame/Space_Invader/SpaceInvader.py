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

playerImg = pygame.image.load('./Pygame/Space_Invader/player1.png')
playerX = 370
playerY = 480

def player():
    #b blit = to draw on screen -> (image, (coordinates))
    screen.blit(playerImg, (playerX, playerY))

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    player()
    pygame.display.update()


#27.07