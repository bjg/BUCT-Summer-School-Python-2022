#in this example we draw a two lines... time progresses but nothing else happens.
#To read the code look first at the main to see what happens in general.
#then look at the functions called by the main to see what they do.
#Thoughtful naming of functions and variables will allow you to read the code more easily

#Challenge:
# 1. Draw a grid
# 2. Change the color of the grid lines 
# 3. Randomly change the color of the entire grid every second
#    Hint: colorGrid and tick need to be changed)

import pygame, sys
from pygame.locals import *
import random

#Number of frames per second
FPS = 4

###Sets size of grid
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

#Check to see if the width and height are multiples of the cell size.
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
#NOTE ON ASSERT - Python's assert statement is a debugging aid that tests a condition.
#If the condition is true, it does nothing and your program just continues to execute. IF False IT WILL SHOW ERROR.
#The assert functions shows there are the correct number of cells for the size of the screen, so we can concentrate on drawing the grid later in program.


#Determine number of cells in horizonatl and vertical plane
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE) # number of cells wide
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE) # Number of cells high

# set up the colours

BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN =    (0,255,0)
RED =    (255,0,0)


################################
# USER Functions CODE in this area
#
#
#
#
#Draws the grid lines
def drawGrid():
    pygame.draw.line(DISPLAYSURF, RED, (10,10),(630,10))
    pygame.draw.line(DISPLAYSURF, RED, (10,10),(10,470))
    pygame.draw.line(DISPLAYSURF, RED, (10,470),(630,470))
    pygame.draw.line(DISPLAYSURF, RED, (630,470),(630,10))

    pygame.draw.line(DISPLAYSURF, BLACK, (20,20),(620,20))
    pygame.draw.line(DISPLAYSURF, BLACK, (20,20),(20,460))
    pygame.draw.line(DISPLAYSURF, BLACK, (20,460),(620,460))
    pygame.draw.line(DISPLAYSURF, BLACK, (620,460),(620,20))
    
#main function
def main():

    #setup the py game defaults.
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Grid example')

    #background color
    DISPLAYSURF.fill(WHITE)

    # Loop until the user clicks the close button.
    done = False
    drawGrid()
    pygame.display.update()
    
    
     
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  
        
        # --- Limit to CONST FPS value for  frames per second
        FPSCLOCK.tick(FPS)
        
    # Close the window and quit.
    pygame.quit()
        
if __name__=='__main__':
    main()
