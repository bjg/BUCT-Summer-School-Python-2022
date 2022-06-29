#in this example we draw a two lines... time progresses but nothing else happens.
#To read the code look first at the main to see what happens in general.
#then look at the functions called by the main to see what they do.
#Thoughtful naming of functions and variables will allow you to read the code more easily

#Challenge:
# 1. Show vector and human at the same time (about 1% of squares for each). 
# 2. Move the humans to the right each tick 
# 3. Build a wall on the right so the humans can't go any further and stop at the wall. 

import pygame, sys
from pygame.locals import *
import random

# Number of frames per second
FPS = 4

#define constants for humans and infected people (vectors) for more readable code
empty = 0
human = 1
vector = 2


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
    if state == 2:
        pygame.draw.rect(DISPLAYSURF, RED, (x, y, CELLSIZE, CELLSIZE))

    return None


##### This is the function that moves time along
# This is where we update the contents of the grid
#
#  1. Go through all of the grid locations
#  2. If there is a human in the locaiton we will try to move them right
#  3.    change the x location by 1 and check if there is a wall
#  4.    if no wall, update the new grid to say there is a human and blank out the current location
#  5.     
def tick(world):
    newTick = world.copy()    # Make a copy of the world to write to. 

         
    return newTick



#Generate random population                                    ######•••••BIG CHANGE HERE WITH NEW VARIABLE••••##
def placeRandomPerson(world, probability, person): ######•••••We got rid of placeRandomhumanswith new variable••##

    for item in world: #for every cell in world 
        count = 0
        if random.uniform(0, 1) < probability: #if a random number beween 0 and 1 is less than probability
            world[item] = person                 #  make the cell a creature
            count += 1
                             
    
    return world    


###••• WE ARE GOING TO BUILD A WALL around the grid•••###
#is a cell inside the world. If it is not then return true, if not return false.
def isNotWall(checkCell):
 
#  Insert your code here checkCell is a tuple  you can access x value with checkCell[0], y value with checkCell[1] 
 
    return False                # This is not a valid grid location
   

#main function
def main():
    
    #    Part 1 - setup the py game defaults.

    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Grid example')

    #background color
    DISPLAYSURF.fill(WHITE)

    #    Part 2 - Populate the world by creating and populating the dictionary.
    
    #This is where our people will live: this is the world
    world = blankGrid() # creates dictionary and populates the grid with empty spaces
 
    # Populate the world using the placeRandomPerson function 
 
    #    Part 3 - Draw the grid and the contents of the grid and display it
    #Colours the cells in the grid at the start of each simulation all will be blank/White for this simulation
    for item in world:
        colourGrid(item, world)

    #draw to the screen the created blank grid
    drawGrid()
    pygame.display.update()


    done = False
    #    Part 4 - loop through the program. This is controlled by the Frames Per second FPS variable
  
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  
        
        # Part 4.1 Update the dictionary that describes the world with any changes we want to make        
        world = tick(world)        

        # Part 4.2 Colour grid based on the updates we made to the dictionary
        for item in world:
            colourGrid(item, world)    
        #draw the grid on the display
        drawGrid()
     
        # Part 4.3 Show the new display on the screen
        pygame.display.update()
        
        # Part 4.4. Wait for the next tick to pass before continuing. The FPS controls the speed of the game
        FPSCLOCK.tick(FPS)


    # Close the window and quit.
    pygame.quit()
        
if __name__=='__main__':
    main()