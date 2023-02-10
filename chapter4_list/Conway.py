#Conway's Game of life

import random, time, copy

WIDTH = 60;
HEIGHT = 20;


def printMatrix(cells):
  for y in range(HEIGHT):
    for x in range(WIDTH):
      print(cells[x][y], end='') # Print the # or space.
  print() # Print a newline at the end of the row.

#create a List for the cells

nextCells= []
for y in range(WIDTH):
  column = [] #create a new column
  for x in range(HEIGHT):
    if random.randint(0, 1) == 0:
      column.append('#') #Add a living cell
    else:
      column.append(' ') #add a dead cell
  nextCells.append(column) #Nexcells add a list of column list

## We have a  20 rows X 60 columns matrix filled with random state cells

while True: #main program
   print('\n') #create a new line for a new step, we can clear screen in this step,google it
   currentCells = copy.deepcopy(nextCells) #clone a new entity seperate from the nextcells and modify this
   printMatrix(currentCells) #print the matrix

   #Calculate the nextstep cells
   for y in range(WIDTH):
      for x in range (HEIGHT):
        #get neighbor coordinate
        #`%WIDTH` ensure leftCoord always stay between 0 and WIDTH -1
        leftCoord = (y - 1) % WIDTH
        rightCoord = (y + 1) % WIDTH
        aboveCoord = (x - 1) % HEIGHT
        belowCoord = (x + 1) % HEIGHT

        #counting living neighbors:
        numNeighbors = 0
        if currentCells[leftCoord][aboveCoord] == '#':
           numNeighbors += 1 #top left is alive
        if currentCells[y][aboveCoord] == '#':
           numNeighbors += 1 #top is alive
        if currentCells[rightCoord][aboveCoord] == '#':
           numNeighbors += 1 #top right is alive
        if currentCells[leftCoord][x] == '#':
           numNeighbors += 1  #left neighbor is alive
        if currentCells[rightCoord][x] == '#':
         numNeighbors += 1  #right neighbor is alive
        if currentCells[leftCoord][belowCoord] == '#':
         numNeighbors += 1 #bottom left is alive
        if currentCells[y][belowCoord] == '#':
         numNeighbors += 1 #bottom is alive
        if currentCells[rightCoord][belowCoord] == '#':
         numNeighbors += 1 #bottom right is alive
        
        # Set cell based on Conway's Game of Life rules:
        if currentCells[y][x] == '#' and (numNeighbors == 2 or numNeighbors == 3):
          nextCells[y][x] = '#'
        elif currentCells[y][x] == ' ' and (numNeighbors == 3):
          nextCells[y][x] = '#'
        else:
          nextCells[y][x] = ' '
        
   time.sleep(0.3)
        