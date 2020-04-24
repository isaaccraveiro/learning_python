import pygame
import random
import sys
import seaborn as sns
import webcolors

note_palette = sns.light_palette("#F0E68C", 12).as_hex()
print("note_palette = ", note_palette)

package_palette = sns.color_palette("Blues_d", 12).as_hex()
print("package_palette = ", package_palette)

manually_gen_palette = sns.light_palette("#5768FF", 12).as_hex()
print("manually_gen_palette   = ", manually_gen_palette)

testing_palette = sns.light_palette("#FBA5A5", 12).as_hex()
print("testing_palette = ",testing_palette)

orm_palette = sns.light_palette("#00ff7f", 12).as_hex()
print("orm_palette = ", orm_palette)

decoration_palette = sns.light_palette("#A0522D", 12).as_hex()
print("decoration_palette = ", decoration_palette)

variability_palette = sns.light_palette("#529999", 12).as_hex()
print("variability_palette = ", variability_palette)

mapping_palette = sns.light_palette("#FFFF00", 12).as_hex()
print("mapping_palette = ", mapping_palette)

templating_palette = sns.light_palette("#ff8c00", 12).as_hex()
print("templating_palette = ",templating_palette)

serialization_palette = sns.light_palette("#00FF00", 12).as_hex()
print("serialization_palette = ",serialization_palette)

visual_studio_palette = sns.light_palette("#006400", 12).as_hex()
print("visual_studio_palette = ", visual_studio_palette)

core_palette = sns.light_palette("#9400d3", 12).as_hex()
print("core_palette = ",core_palette)

pygame.init()

SQUARE_SIZE = 50
WIDTH = SQUARE_SIZE * 11
HEIGHT = SQUARE_SIZE * 12

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


    # for loop
    for i in range(11):
        print("i: ", i)
        rgb = webcolors.hex_to_rgb(note_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 0 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(package_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 1 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(manually_gen_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 2 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(testing_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 3 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(orm_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 4 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(decoration_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 5 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(variability_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 6 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(mapping_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 7 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(templating_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 8 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(serialization_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 9 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(visual_studio_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 10 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        rgb = webcolors.hex_to_rgb(core_palette[i])
        pygame.draw.rect(screen, rgb, (i * SQUARE_SIZE, 11 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    clock.tick(SPEED)

    pygame.display.update()
