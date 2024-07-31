import pygame
from sys import exit

# Initialize pygame
pygame.init()

# Font
font = pygame.font.Font("./assets/font/Pixeltype.ttf", 50)

# Display surface
display = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner!")

# Game surfaces
sky_surface = pygame.image.load("./assets/graphics/sky.png").convert()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()
font_surface = font.render("Game!", False, "Red")
snail_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()

# Snail position
snail_x = 800
snail_y = (300 - 36)

# Clock object
clock = pygame.time.Clock()

while True:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # Snail
    if (snail_x <= 0):
        snail_x = 800
    snail_x -= 5


    # Attaching game display to DS
    display.blit(sky_surface, (0, 0)) # blit: Put one surface on another
    display.blit(ground_surface, (0, 300))
    display.blit(font_surface, (300, 50))
    display.blit(snail_surface, (snail_x, snail_y))

    print(snail_x)

    # Update display surface
    pygame.display.update()

    # Tick rate
    clock.tick(60)
