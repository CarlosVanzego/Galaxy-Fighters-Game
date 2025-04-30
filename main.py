# I start with importing the pygame module
import pygame
# then I am importing the os module
import os
# Here I am initializing the pygame module, font is used to render text on the screen
pygame.font.init()
# Here I am initializing the mixer module of pygame, which is responsible for handling soundplayback
pygame.mixer.init()

# I am setting the width and heigh of the game window to 9000 and 500 respectively
WIDTH, HEIGHT = 900, 500
# win is the variable I created to create the game window using the display module of pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# here I am setting the caption of the game window to "Galaxy Fighters Game!"
pygame.display.set_caption("Galaxy Fighters Game!")
# I created colors using RGB values, this is so that I can use them later in the game; 255, 255, 255 cooresponds to white on the RGB scale
WHITE = ((255, 255, 255))
# 0, 0, 0 cooresponds to black on the RGB scale
BLACK = (0, 0, 0)
# 255, 0, 0 cooresponds to red on the RGB sccale
RED = (255, 0, 0)
# and 255, 255, 0 cooresponds to yellow on th eRGB scale
YELLOW = (255, 255, 0)
# this border variable is used to create a rectangle that will be used as a border between the two players of the game
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# BULLET_HIT_SOUND is used to play the sound when a bullet hits a player 
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets/Grenade+1.mp3'))
# BULLET_FIRE_SOUND is used to play the sound when a bullet is fired
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets/Gun+Silencer.mp3'))
# HEALTH_FONT is used to render the helath of the players on the screen
# I am using the SysFont method to create a font object with the font "comicsans" at size 40
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
# WINNER_FONT is used to render the winner of the game on the screen in the same font but at size 100
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
# FPS is frames per second, which is used to control the speed of the game
FPS = 60
# VEL is the velocity of the players, which is used to control the speed at which the players move 
VEL = 5
# BULLET_VEL is the velocity of the bullets, which is used to control the speed at which the bullets move
BULLET_VEL = 7
# MAX_BULLETS is the maximum number of bullets that can be fired at a time
MAX_BULLETS = 3
# SPACESHIP_WIDTH and SPACESHIP_HEIGHT are the width and height of the spaceships, which are used to create the rectangles for the players
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 40 
# YELLOW_HIT is used to create custom events for when a player is hit by a bullet; this means that when a player is hit by a bullet, the event will be triggered and the health of the player will be decreased; +1 is used to create a unique event ID
YELLOW_HIT = pygame.USEREVENT + 1
# RED_HIT is used to create custom events for when a player is hit by a bullet; this means that when a player is hit by a bullet, the event will be triggered and the health of the player will be decreased; +2 is used to create a unique event ID
RED_HIT = pygame.USEREVENT + 2

# YELLOW_SPACESHIP_IMAGE is used to load the images of the spaceships from the Assets folder
# I am using the os.path.join method to create the path to the image files, which makes it easier to load the images
# I am using the transform method to scale the images to the size of the spaceships and then rotate them to the correct angle
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# RED_SPACESHIP_IMAGE are used to load the images of the spaceships from the Assets folder
# I am using the os.path.join method to create the path to the image files, which makes it easier to load the images
# I am using the transform method to scale the images to the size of the spaceships and then rotate them to the correct angle
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# SPACE is used to load the background image of the game from the Assets folder
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# I defined a function called draw_window that takes in the parameters red, yellos, red_bullets, yellow_bullets, red_health, and yellow_health
# this function is used to draw the game window, which includes the background image, the border between the players, the health of the players, and the spaceships 
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
   # WIN.blit is used to draw the background image on the game window    
   WIN.blit(SPACE, (0, 0))
   pygame.draw.rect(WIN, BLACK, BORDER) 
   # red_health_text and yellow_health_text are used to render the health of the players on the screen 
   red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, RED)
   # yellow_health_text is used to render the health of the players on the screen    
   yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, YELLOW)
   # I am using the blit method to draw the health of the players on th egame window
   # I am alos using the get_width method to get the width of the text so that I can position it correctly on the screen 
   WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
   WIN.blit(yellow_health_text, (10, 10))
   # this line is used to draw the yellow spaceship on the game window 
   WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
   # this line is used to draw the red spaceship on the game window    
   WIN.blit(RED_SPACESHIP, (red.x, red.y))
   # this for loop is used to draw the red bullets on the game window for the yellow spaceship
   for bullet in red_bullets:
       # this line is used to draw the bullets
       pygame.draw.rect(WIN, RED, bullet)
   # this for loop is used to draw the yellow bullets on the game window for the red spaceship    
   for bullet in yellow_bullets:      
       pygame.draw.rect(WIN, YELLOW, bullet)

   # this line is used to update the game window in the event that any changes are made to the game window 
   pygame.display.update()  

#  I defined the function yellow_handle_movement that takes in the parameters keys_pressed and yellow; it is used to handle the movement of the yellow spaceship 
def yellow_handle_movement(keys_pressed, yellow):
    # this line is used to check if the left arrow key is pressed and if the yellow spaceship is not at the left edge of the screen
    # LEFT
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  
        yellow.x -= VEL  
    # this line is used to check if the right arrow key is pressed and if the yellow spaceship is not at the right edge of the screen
    # RIGHT 
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  
        yellow.x += VEL    
    # this line is used to check if the up arrow key is pressed and if the yellow spaceship is not at the top edge of the screen
    # UP 
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  
        yellow.y -= VEL  
    # this line is used to check if the down arrow key is pressed and if the yellow spaceship is not at the bottom edge of the screen
    # DOWN 
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:  
        yellow.y += VEL  

# I defined the function red_handle_movement that takes in the parameters keys_pressed and red; it is usd to handle the movement of the red spaceship
#  
def red_handle_movement(keys_pressed, red):
    # this line is used to check if the left arrow key is pressed and if the red spaceship is not at the left edge of the screen
    # LEFT
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  
        red.x -= VEL  
    # this line is used to check if the right arrow key is pressed and if the red spaceship is not at the right edge of the screen
    # RIGHT 
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  
        red.x += VEL    
    # this line is used to check if the up arrow key is pressed and if the red spaceship is not at the top edge of the screen
    # UP 
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  
        red.y -= VEL  
    # this line is used to check if the down arrow key is pressed and if the red spaceship is not at the bottom edge of the screen
    # DOWN 
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 20:  
        red.y += VEL 

# I defined the function handle_bullets that takes in the parameters yellow_bullets, red_bullets, yellow, and red; it is used to handle the bullets fired by the players
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # this for loop is used to handle the bullets fired by the yellow spaceship
    for bullet in yellow_bullets:
        # bullet.x is used to get the x coordinate of the bullet
        bullet.x += BULLET_VEL
        # this if statement is used to check if the bullet collides with the red spaceship
        if red.colliderect(bullet):
            # this line is used to post the event RED_HIT, which is used to decrease the health of the red spaceship
            pygame.event.post(pygame.event.Event(RED_HIT))
            # this line is used to remove the bullet from the list of bullets
            yellow_bullets.remove(bullet)
        # this line checks if the bullet is out of the screen
        elif bullet.x > WIDTH:
            # this line removes the bullet from the list of bullets
            yellow_bullets.remove(bullet)    
    # this for loop is used to handle the bullets fired by the red spaceship
    for bullet in red_bullets:
        # bullet.x is used to get the x coordinate of the bullet
        bullet.x -= BULLET_VEL
        # this if statement is used to check if the bullet collides with the yellow spaceship
        if yellow.colliderect(bullet):
            # this line is used to post the event YELLOW_HIT, which is used to decrease the health of the yellow spaceship
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            # this line is used to remove the bullet from the list of bullets
            red_bullets.remove(bullet)
        # this line checks if the bullet is out of the screen 
        elif bullet.x < 0:
            # this line removes the bullet from the list of bullets
            red_bullets.remove(bullet)    

#  I defined the draw_winner function that takes in the parameter text; it is used to draw the winner of the game on the screen
def draw_winner(text):
    # the draw_text variable will render the text on the screen in white color 
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    # this line will draw the text on the screen at the center of the game window
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    # this line will update the game window in the event that any changes are made to the game window
    pygame.display.update()
    # this line will wait for 5 seconds before closing the game window (5000 milliseconds = 5 seconds)
    pygame.time.delay(5000)
    
# the main function is used to run the gane
def main():
    # the red variable is used to create a rectangle for the red spaceship 
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    # the yellow variable is used to create a rectangle for the yellow spaceship
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    # I set the red_bullets variable to an empty list, which will be used to store the bullets fired by the red spaceship
    red_bullets = []
    # I set the yellow_bullets variable to an empty list, which will be used to store the bullets fired by the yellow spaceship
    yellow_bullets = []
    # the red_health variable is set to 10, which willl be used to store the health of the red spaceship
    red_health = 10
    # the yellow_health variable is set to 10, which will be used to store the health of the yellow spaceship
    yellow_health = 10
    # the clock variable is used to control the speed of the game
    clock = pygame.time.Clock()
    # I set the run variable to True, which will be used to control the game loop
    run = True
    # this while loop is used to run the game loop
    while run:
        # this lines sets the FPS of the game
        clock.tick(FPS)
        # this for loop is used to check for events in the game
        for event in pygame.event.get():
            # if the event is QUIT, then the game will be closed
            if event.type == pygame.QUIT:
                # run is set to FALSE, which will break the game loop
                run = False
                # this line will quit the game
                pygame.quit()
            # this if statement is used to check if the event is a KEYDOWN event, which means that a key is pressed 
            if event.type == pygame.KEYDOWN:
                # this if statement is used to check if the event is a KEYUP event, which means that a key is released
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    # this line creates the bullet for the yellow spaceship
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    # this line appends the bullet to the list of the yellow bullets 
                    yellow_bullets.append(bullet)
                    # this line plays the sound when the bullet is fired
                    BULLET_FIRE_SOUND.play()
                # this if statement is used to check if the event is a KEYUP event, which means that a key is released
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    # this line creates the bullet for the red spaceship
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    # this line appends the bullet to the list of the red bullets
                    red_bullets.append(bullet) 
                    # this line plays the sound when the bullet is fired
                    BULLET_FIRE_SOUND.play()
            # this if statement is used to check if the event is a YELLOW_HIT event, which means that the yellow spaceship is hit by a bullet
            if event.type == RED_HIT:
                # if it is hit, then the health of the red spaceship is decreased by 1
                red_health -= 1
                # this line plays the sound when the bullet hits the red spaceship
                BULLET_HIT_SOUND.play()
            # this if statement is used to check if the event is a RED_HIT event, which means that the red spaceship is hit by a bullet
            if event.type == YELLOW_HIT:  
                # if it is hit, then the health of the yellow spaceship is decreased by 1
                yellow_health -= 1
                # this line plays the sound when the bullet hits the yellow spaceship
                BULLET_HIT_SOUND.play()
        # this line is used to check if the health of the red spaceship is less than or equal to 0
        winner_text = ""
        # if it is, then the yellow spaceship wins
        if red_health <= 0:
            # and the text "YELLOW WINS!" is displayed on the screen
            winner_text = "YELLOW WINS!"
        # this line is used to check if the health of the yellow spaceship is less than or equal to 0
        if yellow_health <= 0:
            # if it is, then the red spaceship wins and the text "RED WINS!" is displayed on the screen
            winner_text = "RED WINS!" 
        # this if statement is used to check if the winner_text is not empty, which means that the game is over
        if winner_text != "":
            # this line will draw the winner of the game on the screen
            draw_winner(winner_text)
            # this line will break the game loop
            break
        # keys_pressed is used to get the keys that are pressed
        keys_pressed = pygame.key.get_pressed() 
        # this line is used to handle the movement of the yellow spaceship
        yellow_handle_movement(keys_pressed, yellow) 
        # this line is used to handle the movement of the red spaceship
        red_handle_movement(keys_pressed, red) 
        # this line is used to handle the bullets fired by the players
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        # and this line is used to draw the game window
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    # here I am quitting the game   
    main()    
# this if statement is used to check if the script is being run directly from the command line
if __name__ == "__main__":
     # if it is, then the main function is called to run the game    
      main()

