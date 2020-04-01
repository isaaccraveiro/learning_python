import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

COLOUR = (255,123,67)
BACKGROUND = (0,0,0)

player_pos = [400, 300]
player_size = 75

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit(),

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x,y]

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
