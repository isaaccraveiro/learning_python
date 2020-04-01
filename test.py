import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

COLOUR = (255,123,67)
SILVER = (192,192,192)
BACKGROUND = (169,169,169)

player_pos = [700, 500]
player_size = 50

enemy_size = 75
enemy_pos = [100, 25]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:

    for event in pygame.event.get():
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
    pygame.draw.rect(screen,  SILVER, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
