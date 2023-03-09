import random, time, copy
WIDTH = 60
HEIGHT = 20

#create a list of list for the cells:
nextcells = []
for x in range(WIDTH):
 column = []
 for y in range(HEIGHT):
  if random.randint(0, 1) == 0:
   column.append('#') #adding a living cell.
  else:
   column.append(' ') #adding a dead cell.
 nextcells.append(column)
 
while True:
 print('\n\n\n\n\n')
 currentcells = copy.deepcopy(nextcells)
 
 for y in range(HEIGHT):
  for x in range(WIDTH):
   print(currentcells[x][y], end='')
  print()
 for x in range(WIDTH):
  for y in range(HEIGHT):
   leftCoord  = (x - 1) % WIDTH
   rightCoord = (x + 1) % WIDTH
   aboveCoord = (y - 1) % HEIGHT
   belowCoord = (y + 1) % HEIGHT
   numNeighbors = 0
   if currentcells[leftCoord][aboveCoord] == '#':
    numNeighbors += 1
   if currentcells[x][aboveCoord] == '#':
    numNeighbors += 1
   if currentcells[rightCoord][aboveCoord] == '#':
    numNeighbors += 1 # Top-right neighbor is alive.
   if currentcells[leftCoord][y] == '#':
    numNeighbors += 1 # Left neighbor is alive.
   if currentcells[rightCoord][y] == '#':
    numNeighbors += 1 # Right neighbor is alive.
   if currentcells[leftCoord][belowCoord] == '#':
    numNeighbors += 1 # Bottom-left neighbor is alive.
   if currentcells[x][belowCoord] == '#':
    numNeighbors += 1 # Bottom neighbor is alive.
   if currentcells[rightCoord][belowCoord] == '#':
    numNeighbors += 1 # Bottom-right neighbor is alive.
   if currentcells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
    nextcells[x][y] = '#'
   elif currentcells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
    nextcells[x][y] = '#'
   else:
                # Everything else dies or stays dead:
    nextcells[x][y] = ' '
time.sleep(1) # Add a 1-second pause to reduce flickering.
