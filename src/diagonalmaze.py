# Diagonal Maze, by Al Sweigart al@inventwithpython.com
# Prints out a random, diagonal maze.

# Inspired by the 10 PRINT CHR$(205.5+RND(1)); : GOTO 10 program.

import random

FORWARD = chr(9585) # The ╱ character.
BACK    = chr(9586) # The ╲ character.

for x in range(2000): # Loop for each slash in the current line.
    # Randomly add a forward or back slash to the line.
    if random.randint(0, 1) == 0:
        print(FORWARD, end='')
    else:
        print(BACK, end='')
