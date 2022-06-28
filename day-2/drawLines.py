#in this example we draw a two lines... time progresses but nothing else happens.
#To read the code look first at the main to see what happens in general.
#then look at the functions called by the main to see what they do.
#Thoughtful naming of functions and variables will allow you to read the code more easily

#Challenge:
# 1. Change the line colour to RED. 
# 2. Draw a line horizontally across the grid 
# 3. Draw a line vertically down the grid at the same time

import pygame, sys
from pygame.locals import *
import random

# Number of frames per second
FPS = 1

###Sets size of grid
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

#Check to see if the width and height are multiples of the cell size.
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

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
    
# Exclude white so grid doesn't disapear
    lineColour = BLACK   
        
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, lineColour, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, lineColour, (0,y), (WINDOWWIDTH, y))


# Creates an dictionary index of all the cells
# Sets all cells as blank (0 = white)
# Note: The grid is actually a single straight line of values
# the illusion of a grid is achieved by knowing at which value the next line starts
def blankGrid():
    gridDict = {}
    #creates dictionary for all cells
    for y in range (CELLHEIGHT):
        for x in range (CELLWIDTH):
            gridDict[(x,y)] = 0 #Sets cells as white    
    return gridDict

#Colours the cells 
#we can add more rules for different colors
def colourGrid(item, world):

    (xloc,yloc) = item  # This is the grid location to colour sent in the TUPLE item. 
    state = world[item] # here we read the state from the grid location.
    
    
    # work out the coordinates to draw the rectagle so it aligns with the grid.

    y = yloc * CELLSIZE # translates array into grid size
    x = xloc * CELLSIZE # translates array into grid size

    #####********************** ADDED a rule for cells that contain a 1 becoming green

    if state == 1 : 
       pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))
    if state == 0 : 
       pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))


    return None


#
# Here is where we change the display before it is swapped in at the next 
# time the display is updated - this a new frame to display. 
#
# #### This is the function that moves time along
def tick(world,gridPos):

    newTick = world.copy()
   # Green
    newTick[gridPos,gridPos] = 1
    
    return newTick



#main function
def main():

#setup the py game defaults.
    #Our new Grid position variable
    gridPosition = 0
    
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
    world = blankGrid()   #  creates a dictionary which has all values set to white.
    

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  
        
        # --- Limit to CONST FPS value for  frames per second

            
            
        FPSCLOCK.tick(FPS)
        
              
        # Work on updateing the screen before new tick passes
        world = tick(world,gridPosition)
        
        #*********update grid posiytion**************************************************
        gridPosition = gridPosition + 1
  

        #Colours grid based on the value in each cell
        for item in world:
            colourGrid(item, world)
        
        drawGrid()
     
        pygame.display.update() 

    # Close the window and quit.
    pygame.quit()
        
if __name__=='__main__':
    main()
