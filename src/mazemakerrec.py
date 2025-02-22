# Maze Maker by Al Sweigart al@inventwithpython.com
# Implements the recursive backtracker algorithm for making mazes.
# More info at: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
# An animated demo of this algorithm: https://scratch.mit.edu/projects/17358777/

import random

print('MAZE MAKER (Recursive Backtracker algorithm)')
print('By Al Sweigart al@inventwithpython.com')
print()
print('This program creates maze files. You can play these mazes with')
print('mazerunner.py or maze3d.py')

while True:
    response = input('Enter width (must be odd and greater than 2): ')
    if response.isdecimal():
        WIDTH = int(response)
        if WIDTH % 2 == 1 and WIDTH > 2:
            break
while True:
    response = input('Enter height (must be odd and greater than 2): ')
    if response.isdecimal():
        HEIGHT = int(response)
        if HEIGHT % 2 == 1 and HEIGHT > 2:
            break
while True:
    response = input('Enter seed (must be a positive integer): ')
    if response.isdecimal():
        SEED = int(response)
        if SEED >= 0:
            break

random.seed(SEED)

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

# Create the filled-in maze to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL

# Create the maze:
print('Generating maze...')
pathFromStart = [(1, 1)]
hasVisited = [(1, 1)]

while len(pathFromStart) > 0:
    x, y = pathFromStart[-1]
    maze[(x, y)] = EMPTY

    unvisitedNeighbors = []
    # Check the north neighbor:
    if y > 1 and (x, y - 2) not in hasVisited:
        unvisitedNeighbors.append(NORTH)
    # Check the south neighbor:
    if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
        unvisitedNeighbors.append(SOUTH)
    # Check the west neighbor:
    if x > 1 and (x - 2, y) not in hasVisited:
        unvisitedNeighbors.append(WEST)
    # Check the east neighbor:
    if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
        unvisitedNeighbors.append(EAST)

    if len(unvisitedNeighbors) > 0:
        nextIntersection = random.choice(unvisitedNeighbors)
        if nextIntersection == NORTH:
            pathFromStart.append((x, y - 2))
            hasVisited.append((x, y - 2))
            maze[(x, y - 1)] = EMPTY
        elif nextIntersection == SOUTH:
            pathFromStart.append((x, y + 2))
            hasVisited.append((x, y + 2))
            maze[(x, y + 1)] = EMPTY
        elif nextIntersection == WEST:
            pathFromStart.append((x - 2, y))
            hasVisited.append((x - 2, y))
            maze[(x - 1, y)] = EMPTY
        elif nextIntersection == EAST:
            pathFromStart.append((x + 2, y))
            hasVisited.append((x + 2, y))
            maze[(x + 1, y)] = EMPTY
    else:
        pathFromStart.pop()

# Add the start and end positions:
maze[(1, 1)] = START
maze[(WIDTH - 2, HEIGHT - 2)] = EXIT

# Display the maze and save it to a text file.
filename = f'maze{WIDTH}x{HEIGHT}s{SEED}.txt'
mazeFile = open(filename, 'w')

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(maze[(x, y)], end='')
        mazeFile.write(maze[(x, y)])
    print() # Print a newline after printing the row.
    mazeFile.write('\n')
mazeFile.close()

print('Saved to %s.' % (filename))
