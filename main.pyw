import pygame
from sys import exit
import time 

## Initialize pygame
pygame.init()

## Font
font = pygame.font.Font("./assets/font/Pixeltype.ttf", 50)

def display_text(display, font, text, text_color, align, x, y, wrapper=False, wrapper_color="Pink", wrapper_br=5):
    text_surface = font.render(text, False, text_color)
    text_rect = text_surface.get_rect()
    
    if align == 'center':
        text_rect.center = (x, y)
    elif align == 'topleft':
        text_rect.topleft = (x, y)
    elif align == 'topright':
        text_rect.topright = (x, y)
    elif align == 'bottomleft':
        text_rect.bottomleft = (x, y)
    elif align == 'bottomright':
        text_rect.bottomright = (x, y)    
    

    if wrapper:
        text_rect_wrapper = pygame.Rect(text_rect.left - 10, text_rect.top - 10, (10 + text_rect.right - text_rect.left + 10), 10 + (text_rect.bottom - text_rect.top) + 5)
        pygame.draw.rect(display, wrapper_color, text_rect_wrapper, border_radius=wrapper_br) 
        display.blit(text_surface, text_rect)
        return None

    display.blit(text_surface, text_rect)

def draw_text_wrapper(text_rect):
    text_rect_wrapper = pygame.Rect(text_rect.left - 10, text_rect.top - 10, (10 + text_rect.right - text_rect.left + 10), 10 + (text_rect.bottom - text_rect.top) + 5)
    pygame.draw.rect(display, "Pink", text_rect_wrapper, border_radius=5) 

# #----Create display surface----# #
display = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner!")

# #----Game surfaces----# #
sky_surface = pygame.image.load("./assets/graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()
text_surface = font.render("Game!", False, "Red")
snail_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("./assets/graphics/player/player_walk_1.png").convert_alpha()

# #----Rectangles----# #
player_rect = player_surface.get_rect(bottomleft = (50, 300))
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))
text_rect = text_surface.get_rect(center = (400, 50))
text_rect_wrapper = pygame.Rect(text_rect.left - 10, text_rect.top - 10, (10 + text_rect.right - text_rect.left + 10), 10 + (text_rect.bottom - text_rect.top) + 5)

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
i = 0

# #----Vars----# #
player_gravity = 0
allow_double_jump = False
game_acitve = True



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

    
        if game_acitve:
            ## Check for mouse motions
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20


            ## Keyboard input
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if (player_rect.bottom >= 300):
                    player_gravity = -19
                    allow_double_jump = True
                elif (allow_double_jump == True):
                    player_gravity -= 4 
                    # Tow succsive jump clicks ensures maximum height
                    # To get the opposite change -= to = -
                    allow_double_jump = False

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_acitve = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

    ################
    ## Game logic ##
    ################

    # #----Snail movement----# #
    if game_acitve:
        if snail_rect.right <= 0:
            snail_rect.left = 800
        snail_rect.left -= 5
    else:
        snail_rect.left = 800


    # #----Gravity----# #
    player_gravity += 1


    # #----Player movement----# #

    player_rect.bottom += player_gravity


    if (player_rect.bottom >= 300):
        player_rect.bottom = 300
        player_gravity = 0 # This enables to change -= instead of = -20 in event loop for player_gravity


    if (player_rect.top <= 0):
        player_gravity = 25




    ###############
    ## Collision ##
    ###############

    if (player_rect.colliderect(snail_rect) == 1):
        game_acitve = False




    ##########
    ## Blit ##
    ##########

    if game_acitve:

        # #---Bg----# #
        display.blit(sky_surface, (0, 0))
        display.blit(ground_surface, (0, 300))

        # #----Score----# # 
        # pygame.draw.rect(display, "Pink", score_rect)
        # pygame.draw.rect(display, "Pink", text_rect_wrapper, border_radius=5)
        # display.blit(text_surface, text_rect)

        display_text(display, font, "Game!", "Black", "center", 400, 50, True, "Pink", 5)

        # #----Character + npc----# #    
        display.blit(snail_surface, snail_rect)
        display.blit(player_surface, player_rect)
    
    else:
        display.fill("YELLOW")
        display_text(display, font, "'Enter' to continue or 'q' to quit ", "Black", "center", 400, 200)



    # #----Debug----# #
    print(i)
    i += 1


    ################
    ## Essentials ##
    ################

    ## Update display surface
    pygame.display.update()

    ## Tick rate
    clock.tick(60)
