import pygame
import random
import sys
import seaborn as sns
import webcolors

note_palette = sns.light_palette("#F0E68C", 10).as_hex()
print("note_palette = ", note_palette)

package_palette = sns.color_palette("Blues_d", 8).as_hex()
print("package_palette = ", package_palette)

manually_gen_palette = sns.light_palette("#5768FF", 10).as_hex()
print("manually_gen_palette   = ", manually_gen_palette )

# palette = sns.light_palette("#FBA5A5", 1)
# print("testing_palette = ", palette.as_hex())

# palette = sns.light_palette("#00ff7f", 10)
# print("orm_palette = ", palette.as_hex())

# palette = sns.light_palette("#A0522D", 6)
# print("decoration_palette = ", palette.as_hex())

# palette = sns.light_palette("#529999", 10)
# print("variability_palette = ", palette.as_hex())

# palette = sns.light_palette("#FFFF00", 5)
# print("mapping_palette = ", palette.as_hex())

# palette = sns.light_palette("#ff8c00", 3)
# print("templating_palette = ", palette.as_hex())

# palette = sns.light_palette("#00FF00", 2)
# print("serialization_palette = ", palette.as_hex())

# palette = sns.light_palette("#006400", 10)
# print("visual_studio_palette = ", palette.as_hex())

# palette = sns.light_palette("#9400d3", 20)
# print("core_palette = ", palette.as_hex())

pygame.init()

WIDTH = 800
HEIGHT = 600
SQUARE_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

BACKGROUND = (169,169,169)
COLOUR = (255,123,67)
SPEED = 30


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit(),

    screen.fill(BACKGROUND)
    # note palette
    rgb = webcolors.hex_to_rgb(note_palette[0])
    pygame.draw.rect(screen, rgb, (0 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(note_palette[1])
    pygame.draw.rect(screen, rgb, (1 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(note_palette[2])
    pygame.draw.rect(screen, rgb, (2 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(note_palette[3])
    pygame.draw.rect(screen, rgb, (3 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(note_palette[4])
    pygame.draw.rect(screen, rgb, (4 * SQUARE_SIZE,  0, SQUARE_SIZE, SQUARE_SIZE))

    # package palette
    rgb = webcolors.hex_to_rgb(package_palette[0])
    pygame.draw.rect(screen, rgb, (0 * SQUARE_SIZE, 50, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(package_palette[1])
    pygame.draw.rect(screen, rgb, (1 * SQUARE_SIZE, 50, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(package_palette[2])
    pygame.draw.rect(screen, rgb, (2 * SQUARE_SIZE, 50, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(package_palette[3])
    pygame.draw.rect(screen, rgb, (3 * SQUARE_SIZE, 50, SQUARE_SIZE, SQUARE_SIZE))
    rgb = webcolors.hex_to_rgb(package_palette[4])
    pygame.draw.rect(screen, rgb, (4 * SQUARE_SIZE, 50, SQUARE_SIZE, SQUARE_SIZE))

    rgb = webcolors.hex_to_rgb(manually_gen_palette[0])
    pygame.draw.rect(screen, rgb, (0, 50, 0, 50))
  #  rgb = webcolors.hex_to_rgb(package_palette[1])
  #  pygame.draw.rect(screen, rgb, (0, 50, 100, 50))
  #  rgb = webcolors.hex_to_rgb(package_palette[2])
  #  pygame.draw.rect(screen, rgb, (0, 50, 150, 50))
  #  rgb = webcolors.hex_to_rgb(package_palette[3])
  #  pygame.draw.rect(screen, rgb, (0, 50, 200, 50))
  #  rgb = webcolors.hex_to_rgb(package_palette[4])
  # pygame.draw.rect(screen, rgb, (0, 50, 250, 50))
    clock.tick(SPEED)

    pygame.display.update()
