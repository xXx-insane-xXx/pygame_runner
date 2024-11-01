####################
## Import modules ##
####################

import pygame
from sys import exit
from random import randint




################
## Initialize ##
################

# #----Init pygame----# #
pygame.init()

# #----Pygame font----# #
font = pygame.font.Font("./assets/font/Pixeltype.ttf", 50)



####################
## Game functions ##
####################

def display_text(text, text_color, pos_list, wrap=False, wrap_color="Pink", wrap_width=5, wrap_border_radius=5):
    align, x, y = pos_list
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


    if wrap:
        text_wrapper(text_rect, wrap_color, wrap_width, wrap_border_radius)

    display.blit(text_surface, text_rect)


def text_wrapper(text_rect, wrap_color, wrap_width, wrap_border_radius):
    wrap_rect = pygame.Rect(text_rect.left - 10, text_rect.top-10, (text_rect.right+10 - text_rect.left-10)+15, (text_rect.bottom+10 - text_rect.top-10)+15)
    pygame.draw.rect(display, color=wrap_color, rect=wrap_rect, width=wrap_width, border_radius=wrap_border_radius)



def display_score():

    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surface = font.render(f"Score: {current_time}", False, "Black")
    score_rect = score_surface.get_rect()
    score_rect.center = (400, 50)
    text_wrapper(score_rect, "Pink", 0, 10)
    
    display.blit(score_surface, score_rect)
    return current_time



def update_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.left -= 5

        obstacle_rect_list = [obstacle_rect for obstacle_rect in obstacle_rect_list if obstacle_rect.x > -100]
        return obstacle_rect_list

    else:
        return []
    


def blit_obstacle(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            if obstacle_rect.bottom == 300:
                display.blit(snail_surface, obstacle_rect)
            else:
                display.blit(fly_surface, obstacle_rect)



def is_collide(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            if player_rect.colliderect(obstacle_rect):
                return True
    return False


def player_animation():
    global player_surface, player_index
    
    if player_rect.bottom < 300:
        player_surface = player_jump_surface
    else:
        player_index += 0.1
        if player_index >= len(player_walk_surface_list):
            player_index = 0
        player_surface = player_walk_surface_list[int(player_index)]


    



#############################
## Game surfaces and rects ##
#############################

# #---- Create display surface ----# #
display = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner!")


# #---- Game surfaces ----# #
sky_surface = pygame.image.load("./assets/graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()

player_walk_1_surface = pygame.image.load("./assets/graphics/player/player_walk_1.png").convert_alpha()
player_walk_2_surface = pygame.image.load("./assets/graphics/player/player_walk_2.png").convert_alpha()
player_walk_surface_list = [player_walk_1_surface, player_walk_2_surface]
player_index = 0
player_jump_surface = pygame.image.load("./assets/graphics/player/player_walk_1.png").convert_alpha()
player_surface = player_walk_surface_list[player_index] # Picks walk_1 by default as player_index is set to 0

player_stand_surface = pygame.image.load("./assets/graphics/player/player_stand.png").convert_alpha()

snail_1_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()
snail_2_surface = pygame.image.load("./assets/graphics/snail/snail2.png").convert_alpha()
snail_index = 0
snail_surface_list = [snail_1_surface, snail_2_surface]
snail_surface = snail_surface_list[snail_index]

fly_1_surface = pygame.image.load("./assets/graphics/fly/fly1.png").convert_alpha()
fly_2_surface = pygame.image.load("./assets/graphics/fly/fly2.png").convert_alpha()
fly_index = 0
fly_surface_list = [fly_1_surface, fly_2_surface]
fly_surface = fly_surface_list[fly_index]

font_surface = font.render("Game", False, "Black")


# #---- Game rectangles ----# #
sky_rect = sky_surface.get_rect(topleft=(0, 0))
ground_rect = ground_surface.get_rect(topleft=(0, 300))

player_walk_1_rect = player_walk_1_surface.get_rect(bottomleft = (50, 300))
player_walk_2_rect = player_walk_2_surface.get_rect(bottomleft = (50, 300))
player_rect = player_surface.get_rect(bottomleft = (50, 300))

snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

font_rect = font_surface.get_rect(midbottom = (400, 50))

player_stand_rect = player_stand_surface.get_rect(center = (400, 200))




##########################################
## Other required objects and variables ##
##########################################

# #---- Clock ----# #
clock = pygame.time.Clock()


# #---- Vars ----# #
game_active = False
player_gravity = 0
start_time = 0
score = 0
start_screen = True
obstacle_rect_list = []


# #---- Event ----# #
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) # 900 ms

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 100)



##########
## Note ##
##########
'''

Player animation has been done using a dedicated function (player_animation) and without timer 
based method, to show only walk_image_2 specifically while player is jumping.

Using a timer here, might show walk_surface_1 during jump due to a slight delay in the event getting 
triggered and player_surface variable not being timely updated.

This gives more control over the animation, if we are dealing with multiple states, which is not
the case for obstacles.


'''


###############
## Game loop ##
###############

while True:

    events = pygame.event.get()

    for event in events:

        ## Check for quit
        if event.type == pygame.QUIT:
            exit()

        
        ## Start game screen
        if start_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_time = int(pygame.time.get_ticks() / 100)
                game_active = True
                start_screen = False

        
        ## Running game
        if game_active:
            ## Check for jump input
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_gravity = -20
            
            ## Fill in obstacle_rect_list
            if event.type == obstacle_timer:
                if randint(0, 1):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomleft = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomleft = (randint(900, 1100), 210)))

            
            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0

                snail_surface = snail_surface_list[snail_index]



            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0

                fly_surface = fly_surface_list[fly_index]


            ## For devs
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
                game_active = False
    
        else:
            ## Continue game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_time = int(pygame.time.get_ticks() / 100)
                game_active = True
            
            ## Quit game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                exit()




    ################
    ## Game logic ##
    ################
    

    # #----Reset----# #
    if not game_active:
        player_rect.bottomleft = (50, 300)
        obstacle_rect_list.clear()
        player_gravity = 0


    # #----Gravity----# #
    player_rect.bottom += player_gravity
    player_gravity += 1
    
    ## Safe gaurd to avoid memory consumption
    if player_gravity >= 10000:
        player_gravity = 0


    # #----Player movement----# #
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    if (pygame.key.get_pressed()[pygame.K_RIGHT]):
        if (player_rect.right > 200):
            player_rect.right = 200
        player_rect.right += 5

    if (pygame.key.get_pressed()[pygame.K_LEFT]):
        if (player_rect.left < 0):
            player_rect.left = 0
        player_rect.left -= 5



    ###############
    ## Collision ##
    ###############

    if is_collide(obstacle_rect_list):
        game_active = False




    ##########
    ## Blit ##
    ##########
    
    if game_active:
        ## Bg
        display.blit(sky_surface, sky_rect)
        display.blit(ground_surface, ground_rect)
        
        ## Player + obstacles
        player_animation()
        display.blit(player_surface, player_rect)
        obstacle_rect_list = update_movement(obstacle_rect_list)
        blit_obstacle(obstacle_rect_list)
        
        ## Score
        score = display_score()

    else:
        display.fill((94, 129, 162))
        display.blit(player_stand_surface, player_stand_rect)
        
        ## To display during start game screen
        if start_screen:
            display_text("Pixel Runner", "Black", ["center", 400, player_stand_rect.top - 50])
            display_text("Press Enter to Play!!", "Black", ["center", 400, player_stand_rect.bottom + 50])

        ## To display when player and obstacle collide
        else:
            display_text(f"Your current score {score}", "Black", ["center", 400, player_stand_rect.top - 50])
            display_text("'Enter' to continue or 'q' to quit ", "Black", ["center", 400, player_stand_rect.bottom + 50])




    ##########
    ## Logs ##
    ##########

    # print(score)



    ####################
    ## Update and fps ##
    ####################
    
    ## Update display surface
    pygame.display.update()

    ## Tick rate
    clock.tick(60)
