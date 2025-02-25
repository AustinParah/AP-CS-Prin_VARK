import random
import math

# Student name

# determine the best next step given a starting point and target location
def next_step(currentX, currentY, targetX, targetY):
    
    # assume no step possible
    step = (currentX,currentY)    
    
    # STUDENT CODE HERE
    tX = targetX
    tY = targetY

    cY = currentY
    cX = currentX

    offsets = [-1, 0, 1]

    low_oX = 0
    low_oY = 0

    lowest = 1000000
    for oX in offsets:
        for oY in offsets:
            distance = math.sqrt((oX+cX-tX)*(oX+cX-tX) + (oY+cY-tY)*(oY+cY-tY))
            if(distance < lowest):
                lowest = distance
                low_oX = oX
                low_oY = oY
    
    step = (low_oX + cX, low_oY + cY)
    
    # END STUDENT CODE
    return step

# NO STUDENT CHANGES BELOW THIS LINE

# display the current grid with positions of all 3 objects
def draw_grid(catX,catY,mouseX,mouseY,cheeseX,cheeseY):
    print("  012345")
    for row in range(0,6):
        print(row,end=" ")
        for col in range(0,6):
            if col == catX and row == catY:
                print("C",end="")
            elif col == mouseX and row == mouseY:
                print("M",end="")
            elif col == cheeseX and row == cheeseY:
                print("X",end="")
            else:
                print(".",end="")
        print()

# calculate the distance between two points
def calculate_distance(x1,y1,x2,y2):
    # Pythagorean's Theorem
    distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    return distance

# main program logic starts here

# seed the random number generator
grid = int(input("Enter grid number: "))
random.seed(grid)

# calculate starting cat, mouse, and cheese locations
catX = random.randrange(0,6)
catY = random.randrange(0,6)

mouseX = random.randrange(0,6)
mouseY = random.randrange(0,6)

cheeseX = random.randrange(0,6)
cheeseY = random.randrange(0,6)

# draw initial grid
draw_grid(catX,catY,mouseX,mouseY,cheeseX,cheeseY)

# run algorithm to find next step for cat and mouse
cat_step = next_step(catX,catY,mouseX,mouseY)
mouse_step = next_step(mouseX,mouseY,cheeseX,cheeseY)

# update current cat and mouse positions
catX = cat_step[0]
catY = cat_step[1]
mouseX = mouse_step[0]
mouseY = mouse_step[1]

print("Cat   moves to (" + str(catX) + "," + str(catY) + ")")
print("Mouse moves to (" + str(mouseX) + "," + str(mouseY) + ")")

# draw final grid after cat and mouse each take a step
draw_grid(catX,catY,mouseX,mouseY,cheeseX,cheeseY)

