#in this example we draw a two lines... time progresses but nothing else happens.
#To read the code look first at the main to see what happens in general.
#then look at the functions called by the main to see what they do.
#Thoughtful naming of functions and variables will allow you to read the code more easily

#Challenge:
# 1. Create a dictionary in the blankGrid function which holds the state for each grid location
# 2. Draw a rectangle in a specific grid location using colourGrid 
# 3. Update the tick function to Make one of the grid locations flash on and off every second

import pygame, sys
from pygame.locals import *
import random

# Number of frames per second
FPS = 1

###Sets size of grid
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

# if the cells are 10 wide then there are 64 cells across
# if the cells are 10 long then there are 48 cells down

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
    # the format of the gridDict is (x,y) : state.
    
    # Create a loop that sets up the grid so that there are 64 grid locations wide
    # and there are 48 grid locations down all with a value of 0. Now we have a colour state in each
    # grid location, set to 0 (white). 
    
    x=0
    y=0
    gridDict[(x,y)] = 0 #Sets cells as white
    
    
    return gridDict

#Colours the cells 
#we can add more rules for different colors
# item:  a specific tuple in the dictionary
# world: the dictionary we are using which holds the state for each grid location

def colourGrid(item, world):

    (xloc,yloc) = item  # This is the grid location to colour sent in the TUPLE item. 
    state = world[item] # here we read the state from the grid location. 
    
    # work out the coordinates to draw the rectagle so it aligns with the grid.

    # This is the draw rectangle command, it will draw rectangle at screen coordinates x,y by a set width and height
    # pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, width, height))

    return None


#
# Here is where we change the display before it is swapped in at the next 
# time the display is updated - this a new frame to display. 
#
# #### This is the function that moves time along
def tick(world):

    newTick = world.copy()
    
    #insert code to turn the grid position [1,2] into one colour
    #then back to white each
    #time this function is called
    
    
    return newTick
         
         
         
         
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
    world = blankGrid()   #  creates a dictionary which has all values set to white.
    
    world[(1,2)] = 1  #  set this grid location to state 1 = GREEN
    world[(1,3)] = 1  #  set this grid location to state 1 = GREEN

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  
        
        # --- Limit to CONST FPS value for  frames per second
        FPSCLOCK.tick(FPS)
 
        # Work on updateing the screen before new tick passes
        #world = tick(world)
        
        
        #Colours grid based on the value in each cell
        for item in world:
            colourGrid(item, world)
        
        drawGrid()
     
        pygame.display.update() 

    # Close the window and quit.
    pygame.quit()
        
if __name__=='__main__':
    main()
