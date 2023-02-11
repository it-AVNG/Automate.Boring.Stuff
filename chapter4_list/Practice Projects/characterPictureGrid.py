#Say you have a list of lists where each value in the inner lists is a one-character string
#Copy the previous grid value, and write code that uses it to print the image, start with 8x8

import random, copy, os, time

HEIGHT=8
WIDTH=8
frame=[]
#clear the screen
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

#a function to add the value
def randomValue():
    result = random.randint(0,1)
    if result == 0:
      return '.'
    else:
       return 'o'

#main program

clear()
for y in range(HEIGHT):
  column = [] #make a new column
  for x in range(WIDTH):
    column.append(randomValue())
  frame.append(column)

grid = copy.deepcopy(frame)

for y in range(HEIGHT):
  for x in range(WIDTH):
    print(grid[x][y], end = ' ')
  print()
  

