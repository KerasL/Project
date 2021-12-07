# Final version of game
# xxx
# ICS Culminating Project: a fisherman game to accumulate scores when fish are caught

#Import & initialize the pygame module
import pygame
import random
import sys
import math
import platform

#pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for events. 
#It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP
from pygame.locals import *  
# better use pygame.MOUSEMOTION

#This will allow us to name the colours to use rather than give a name  eg (255,0,0)
from pygame.color import THECOLORS

# initial library itself
pygame.init()  

#Just like python, we will use os and time????
import os, time

#this code is necessary for python to work on tdsb computers
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Set-up the main screen display window and caption  in the 
size = (650, 650)  
screen = pygame.display.set_mode(size) 

#Puts a caption in the bar at the top of the window
pygame.display.set_caption("Fishing Game!") 

clock = pygame.time.Clock()
#set timer to specific time and to count down
counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
bigfont = pygame.font.SysFont("Consolas", 40)

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

# A procedure to display the background
def background():
    bg = pygame.image.load("images/background1.png")
    bg = pygame.transform.scale(bg, (650,650))
    screen.blit(bg, (0,0))
    myfont = pygame.font.SysFont("Cuckoo",50)
    fishing = myfont.render(('Let\'s go FISHING'), True, (100,255,255))
    screen.blit(fishing,(150,100)) 
    
# A procedure to display the game background
def gamebackground():
    a=200
    b=28
    backg = pygame.image.load('images/game.jpg')
    backg = pygame.transform.scale(backg, (650,650))
    screen.blit(backg, (0,0))
    screen.blit(player, (a, b))
    
# A function to display points
def points(count):
    font = pygame.font.SysFont('Consolas', 24)
    text = font.render ("Points:"+str(count), True, (0,0,0))
    screen.blit(text, (500,20))    

# Main Program

x=30
y=30
count = 0 
# All fish images in two lists
randpicList=["images/a.gif","images/b.gif","images/c.gif","images/d.gif","images/e.gif", "images/f.gif", "images/g.gif", "images/h.gif", "images/i.gif", "images/j.gif"] 
randpic1List=["images/a1.gif","images/b1.gif","images/c1.gif","images/d1.gif","images/e1.gif","images/f1.gif","images/g1.gif","images/h1.gif","images/i1.gif","images/j1.gif"]
fishR=[]
fishL=[]
pixelsMove=[]
pixelsMove1=[]
updown=[]
topX=[]
topX1=[]

# display the fisherman image
player=pygame.image.load("images/fisherman.jpg").convert()
# Backgroumd Music
mainMusic = pygame.mixer.music.load("audio/8-bitDetective.wav")
pygame.mixer.music.play(-1,0.0)

#List added by using random fish images, random speed of fish and random location for fish
for i in range(5):
    fishL.append(pygame.image.load(random.choice(randpicList)).convert())
    fishR.append(pygame.image.load(random.choice(randpic1List)).convert())
    pixelsMove.append(random.randint(-10,-1))
    pixelsMove1.append(random.randint(1,10))
    topX.append(random.randint(25,40))
    topX1.append(random.randint(25,40))
    updown.append(0)
    
updown[0]=random.randint(200,230)
updown[1]=random.randint(240,280)
updown[2]=random.randint(290,350)
updown[3]=random.randint(360,475)
updown[4]=random.randint(500,600)

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

# Set up desired font 
myfont = pygame.font.SysFont("Cuckoo", 25)
font = pygame.font.SysFont("Cuckoo", 26)

# Initialize the default state and game mode
state="menu"
game = "go"

# Load image or start game, instruction and exit option button
btnStart=pygame.image.load("images/startgame1.jpg").convert()
btnInrtuct=pygame.image.load("images/instructions.jpg").convert()
btnExit=pygame.image.load("images/quit.jpg").convert()

#variables for text throughout the game
keyinst = font.render(("This nice fisherman needs help catching fish! "), True, (0,0,0))
keyinst1 = font.render(("Help him catch as many fish as you can in the "), True, (0,0,0))
keyinst2 = font.render (("span of 30 seconds by clicking on the fish!~"), True, (0,0,0))
welcome = myfont.render(('WELCOME TO MY GAME'), True, (255,255,255))
instruct = myfont.render(('How to play:'), True, (0,0,0))
error = myfont.render(('Error!!!!!!!!!'), True, (200,0,10))
time = bigfont.render(("TIME'S UP!"),True, (0,0,0))
end = myfont.render (("You caught "), True, (0,0,0))
fih = myfont.render (("fish"), True, (0,0,0))
playagain = font.render (("Play again"), True, (0,0,0))
main = font.render (("Main Menu"), True, (0,0,0))
back = font.render (("Back"), True, (0,0,0))


try:
    while keepGoing:
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second  
 
        if state=="menu":
                background()
           # Buttons-------------------
                bn=screen.blit(btnStart,(150,465))    #bn- rectangle arround button btnNew
                bi=screen.blit(btnInrtuct,(425,480))    #bi- rectangle arround button btnInrtuct
                be=screen.blit(btnExit,(300,550))      #be- rectangle arround button btnExit
                
                # Handle any events in the current frame
                for ev in pygame.event.get():
                    # Based on the option chosen by the user, either change the keepGoing mode or set the state
                    if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                        keepGoing = False
                    elif ev.type == MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        if bn.collidepoint(pos):
                            state="game"
                        elif bi.collidepoint(pos):
                            state="instructuctions"
                        elif be.collidepoint(pos):
                            keepGoing = False

        # If the user chooses to Start Game
        elif state=="game":  
            gamebackground ()
            
            # Check the game mode
            if game == "go":
                for ev in pygame.event.get():
                    if ev.type == pygame.USEREVENT: 
                        counter -= 1
                        text = str(counter).rjust(3) if counter > 0 else 'Time\'s Up!'
                    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
                    points(count)
                    if ev.type == pygame.QUIT:  #<-- this special event type happens when the window is closed
                        keepGoing = False
                    elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        pos=ev.pos
                        print( "You pressed the left mouse button at", pos[0], pos[1])  #pos[0] - x inate   pos[1] - y coordinate
                    elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                        print( "You released the left mouse button at " ,ev.pos[0],ev.pos[1])
                        if pos[0]> topX[0]-1 and pos[0] < topX[0] +150 and pos[1]>updown[0]-10 and pos[1] < updown[0] +100:
                            count +=1
                        elif pos[0]> topX[1]-1 and pos[0] < topX[1] +150 and pos[1]>updown[1]-10 and pos[1] < updown[1] +100:
                            count +=1 
                        elif pos[0]> topX[2]-1 and pos[0] < topX[2] +150 and pos[1]>updown[2]-10 and pos[1] < updown[2] +100:
                            count +=1 
                        elif pos[0]> topX[3]-1 and pos[0] < topX[3] +150 and pos[1]>updown[3]-10 and pos[1] < updown[3] +100:
                            count +=1 
                        elif pos[0]> topX[4]-1 and pos[0] < topX[4] +150 and pos[1]>updown[4]-10 and pos[1] < updown[4] +100:
                            count +=1 
                        elif pos[0]> topX1[1]-1 and pos[0] < topX1[1] +150 and pos[1]>updown[1]-10 and pos[1] < updown[1] +100:
                            count +=1 
                        elif pos[0]> topX1[0]-1 and pos[0] < topX1[0] +150 and pos[1]>updown[0]-10 and pos[1] < updown[0] +100:
                            count +=1 
                        elif pos[0]> topX1[2]-1 and pos[0] < topX1[2] +150 and pos[1]>updown[2]-10 and pos[1] < updown[2] +100:
                            count +=1 
                        elif pos[0]> topX1[3]-1 and pos[0] < topX1[3] +150 and pos[1]>updown[3]-10 and pos[1] < updown[3] +100:
                            count +=1 
                        elif pos[0]> topX1[4]-1 and pos[0] < topX1[4] +150 and pos[1]>updown[4]-10 and pos[1] < updown[4] +100:
                            count +=1
                    print (count)
                    if counter == 0:
                        game ="stop"
                clock.tick(60) 
                for i in range(5):
                    if topX[i] <= 0-100:
                        topX[i]=650+50
                    if topX1[i]>=650:
                        topX1[i]=-150
                    topX[i]+=pixelsMove[i]
                    topX1[i]+=pixelsMove1[i]
                    screen.blit(fishL[i], (topX[i], updown[i]))
                    screen.blit(fishR[i], (topX1[i], updown[i]))
                    pygame.display.flip()
            
            elif game == "stop":
                gamebackground ()
                pygame.display.flip()
                screen.blit(time, (250,200))
                screen.blit (end, (300, 240))
                score = bigfont.render (str(count), True, (0,0,0))
                screen.blit (score, (325,260))
                screen.blit (fih, (325, 295))
                screen.blit(playagain, (20, 599))
                screen.blit(main, (555,598))
                for ev in pygame.event.get():
                    if ev.type == MOUSEBUTTONDOWN:
                        x, y=pygame.mouse.get_pos()
                        print (x)
                        if x >15 and x < 110 and  y > 580 and y  < 610:
                            state="game"
                            game = "go"
                            count = 0
                            counter = 30
                            
                        elif x > 560 and x < 620 and y > 590 and y< 620:
                            state="menu"
                            count = 0    # reset the initial score back to zero
                            counter = 30   # reset the timer back to 30 seconds
                        
        elif state=="instructuctions":
            background ()
            pygame.display.flip()
            screen.blit (back, (20, 599))
            # ---------------code for the instructions-------------------
            screen.blit(instruct, (180,470))   # print text instructions
            screen.blit(keyinst, (180, 500))
            screen.blit(keyinst1, (180, 515))
            screen.blit(keyinst2, (180, 530))
            for ev in pygame.event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    x, y=pygame.mouse.get_pos()
                    if x >15 and x < 110 and  y > 580 and y  < 610:
                        state="menu"
            
        else:
            screen.blit(error, (20,60))       # print text error

        pygame.display.flip()
       
finally:
    pygame.quit()  # Keep this IDLE friendly 



