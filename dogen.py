import pygame
import random
import sys
import seaborn as sns
import webcolors

note_palette = sns.light_palette("#F0E68C", 10).as_hex()
print("note_palette = ", note_palette)

#palette = sns.light_palette("gray", 20)
# print("package_palette = ", palette.as_hex()[:10])

note_palette = sns.light_palette("#5768FF", 10).as_hex()
print("note_palette = ", note_palette)

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
    rgb = webcolors.hex_to_rgb(note_palette[0])
    pygame.draw.rect(screen, rgb, (100, 0, 50, 50))
    rgb = webcolors.hex_to_rgb(note_palette[1])
    pygame.draw.rect(screen, rgb, (0, 0, 50, 50))
    rgb = webcolors.hex_to_rgb(note_palette[2])
    pygame.draw.rect(screen, rgb, (50, 0, 50, 50))
    rgb = webcolors.hex_to_rgb(note_palette[3])
    pygame.draw.rect(screen, rgb, (150, 0, 50, 50))
    rgb = webcolors.hex_to_rgb(note_palette[4])
    pygame.draw.rect(screen, rgb, (200, 0, 50, 50))

    clock.tick(SPEED)

    pygame.display.update()
