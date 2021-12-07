# imports pygame and time
import pygame
import time
# initializes pygame
pygame.init()

# declares clock
clock = pygame.time.Clock()

# defines some colours
gray = (80, 80, 80)
light_gray = (200, 200, 200)
white = (255, 255, 255)
darkblue = (33, 36, 46)
black = (0, 0, 0)

# defines game display
size = (1100, 800)
gameDisplay = pygame.display.set_mode(size)

# sets the caption and icon
pygame.display.set_caption("The Tutorial")


# loads background images
title_background= pygame.image.load("titleBackground.jpg")
title_background = pygame.transform.scale(title_background, size)
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,size)
background_level1 = pygame.image.load("gameBackground.jpg")
background_level1 = pygame.transform.scale(background_level1, size)
lessons = pygame.image.load("instructions.jpg")
lessons = pygame.transform.scale(lessons, size)

#declares some variables 
unlocked = False
score = 10000
# openchest = False

#allows text to be displayed
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# defines message display
def message_display(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 75)
    
#button function   
def button(msg, x, y, w, h, inactive_colour, active_colour, action, fontsize):

    #Defines mouse, as the coodinates of the mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #checks if the mouse is within the coordinates of the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        #draws the button in the active colour
        pygame.draw.rect(gameDisplay, active_colour, (x, y, w, h))
        #checks if the left mouse is pressed
        if click[0] == 1:
            #performs action based on the button's said function
            if action == "animation":
                animation()
            if action == "lessons":
                lesson()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "main_menu":
                main_menu()

    #if the mouse is not within the coordinates of the button, it draws the button in it's inactive colour
    else:
        pygame.draw.rect(gameDisplay, inactive_colour, (x, y, w, h))
    #draws text on the button
    smallText = pygame.font.Font("freesansbold.ttf", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    #Centers the text on the button
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

#*****************************************************************
# Title screen loop
def TitleScreen():
    TitleScreen = True
    x = 0
    y = 0    
    while TitleScreen:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(title_background, (0,0))
        
        # Title of project
        myfont = pygame.font.SysFont("Cuckoo",50)
        project = myfont.render(("Game"), True, white)
        name = myfont.render(("Tom Liu"), True, white)
        date = myfont.render(("June 15, 2015"), True, white)
        course = myfont.render(("ICS2O1"), True, white)
        gameDisplay.blit(project,(800,175))   
        gameDisplay.blit(name,(800,225))  
        gameDisplay.blit(date,(800,275))  
        gameDisplay.blit(course,(800,325)) 
     
        # Button and button text
        mouse = pygame.mouse.get_pos() # mouse position coordinates
        click = pygame.mouse.get_pressed() # click coordinates
        
        if 650 + 125 > mouse[0] > 650 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, darkblue, (675, 500, 100, 50))
            if click[0] == 1:
                main_menu()
        else:
            pygame.draw.rect(gameDisplay, darkblue, (675, 500, 100, 50))
        
        next = myfont.render(("Next"), True, (100,255,255))
        gameDisplay.blit(next,(690, 510)) 
        # Update display
        pygame.display.update()        
        clock.tick(60)

#______________________________________________________________________________________
#defines the main menu/lobby for the game
def main_menu():

    tutorial = True
    #creates loop for the game
    while tutorial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # draws background image
        gameDisplay.blit(background, (0, 0))

        #draws buttons
        button("Start animation", 50, 325, 250, 100, gray, light_gray, "animation", 32) 
        button("Lessons", 50, 450, 250, 100, gray, light_gray, "lessons", 32)
        button("Quit", 50, 575, 250, 100, gray, light_gray, "quit", 32)                                 
        #updates the display
        pygame.display.flip()
        clock.tick(60)

#defines the lessons page        
def lesson():
    animation = True
    #creates a loop for the game
    while animation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        #blits the background 
        gameDisplay.blit(lessons, (0, 0))
        #button to return to main menu
        button("Back", 800, 650, 250, 100, gray, light_gray, "main_menu", 40)

        #updates the display
        pygame.display.flip()
        clock.tick(60)
        
def animation():
    animation = True
    #creates a loop for the animation
    while animation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
        message_display("This is your tutorial")
        #draws the background and images 
        gameDisplay.blit(background_level1, (0, 0))

        ########################################################
        # Your working animation should go here.
        
        

        ##########################################################        
        #button to return to main menu
        button("Back", 800, 650, 250, 100, gray, light_gray, "main_menu", 40)        
        
        #updates the display
        pygame.display.flip()
        clock.tick(60)
    

def tutorialLoop():
    tutorialExit = False
    #creates loop for the tutorial
    while tutorialExit == False:
        main_menu()

TitleScreen()