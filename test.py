import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

COLOUR = (255,123,67)
SILVER = (192,192,192)
BACKGROUND = (169,169,169)
SPEED = 35

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
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
         if (e_y >= p_y and e_y < (p_y + player_size))or (p_y >= e_y and p_y <(e_y + enemy_size)):
            return True
    return False

def detect_collision_isaac(player_pos, enemy_pos):
    p_x_0 = player_pos[0]
    p_y_0 = player_pos[1]
    p_x_1 = player_pos[0] + player_size
    p_y_1 = player_pos[1] + player_size

    e_x_0 = enemy_pos[0]
    e_y_0 = enemy_pos[1]
    e_x_1 = enemy_pos[0] + enemy_size
    e_y_1 = enemy_pos[1] + enemy_size

    if (e_x_0 >= p_x_0 and e_x_0 < p_x_1) or (p_x_0 >= e_x_0 and p_x_0 < (e_x_1)):
         if (e_y_0 >= p_y_0 and e_y_0 < p_y_1) or (p_y_0 >= e_y_0 and p_y_0 < e_y_1):
            return True
    return False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit(),

        if event.type == pygame.KEYDOWN:
            print("key down")
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                print("key left")
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                print("key right")
                x += player_size

            player_pos = [x,y]

    screen.fill(BACKGROUND)
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        print("move enemy: ", enemy_pos[1])
        enemy_pos[1] += 20
    else:
        print("new enemy")
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        enemy_pos[1] = 1

    if detect_collision_isaac(player_pos,enemy_pos):
        print("game over")
        COLOUR = (155,123,67)
        game_over = True
        break

    pygame.draw.rect(screen,  SILVER, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(SPEED)

    pygame.display.update()
