import pygame
import random
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
enemy_pos = [random.randint(0,WIDTH-enemy_size), 25]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_x = enemy_pos[1]

    #f e_x >= p_x and e_x < (p_x + player_size) or(p_x >= e_x and p_x <(e_x+enemy_size))

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
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
        enemy_pos[1] = 1
    pygame.draw.rect(screen,  SILVER, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(35)

    pygame.display.update()
