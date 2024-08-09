import pygame
from sys import exit

## Initialize pygame
pygame.init()

## Font
font = pygame.font.Font("./assets/font/Pixeltype.ttf", 50)

# #----Create display surface----# #
display = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner!")

# #----Game surfaces----# #
sky_surface = pygame.image.load("./assets/graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()
score_surface = font.render("Game!", False, "Red")
snail_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("./assets/graphics/player/player_walk_1.png").convert_alpha()

# #----Rectangles----# #
player_rect = player_surface.get_rect(bottomleft = (50, 300))
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))
score_rect = score_surface.get_rect(center = (400, 50))
score_rect_wrapper = pygame.Rect(score_rect.left - 10, score_rect.top - 10, (10 + score_rect.right - score_rect.left + 10), 10 + (score_rect.bottom - score_rect.top) + 5)

# #----Pos----# #
## Snail initial pos
snail_xPos = 800
snail_yPos = 300 - 36

## Player pos
player_xPos = 50
player_yPos = 300 - 84

## Clock object
clock = pygame.time.Clock()

# #----Global test----# #
counter = 0




##########
## Core ##
##########

while (True):

    ################
    ## Event loop ##
    ################

    events = pygame.event.get()
    for event in events:

        ## Check for exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        ## Check for mouse motions
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("Mouse is hovering over the player")




    ################
    ## Game logic ##
    ################

    # #----Snail movement----# #
    if snail_rect.right <= 0:
        snail_rect.left = 800
    snail_rect.left -= 5

    # #----Player movement----# #




    ###############
    ## Collision ##
    ###############

    if (player_rect.colliderect(snail_rect) == 2):
        print("Collision")




    ##########
    ## Blit ##
    ##########

    # #---Bg----# #
    display.blit(sky_surface, (0, 0))
    display.blit(ground_surface, (0, 300))

    # #----Score----# # 
    # pygame.draw.rect(display, "Pink", score_rect)
    pygame.draw.rect(display, "Pink", score_rect_wrapper, border_radius=5)
    display.blit(score_surface, score_rect)

    # #----Character + npc----# #    
    display.blit(snail_surface, snail_rect)
    display.blit(player_surface, player_rect)




    ################
    ## Essentials ##
    ################

    ## Update display surface
    pygame.display.update()

    ## Tick rate
    clock.tick(60)
