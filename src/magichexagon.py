# Magic Hexagon, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Magic_hexagon
# More info at https://www.youtube.com/watch?v=ZkVSRwFWjy0

import sys

# Print the title and instructions:
print('Welcome to Magic Hexagon!')
print('-------------------------')
print('Place the numbers 1 to 19 on spaces A through S such that all 15')
print('horizontal and diagonal rows add up to 38.')
print()
input('Press enter to begin...')

# A large, multi-line string that acts as a template for the game board:
# You can copy/paste this from https://pastebin.com/raw/h9ufKzSz
boardTemplate = r"""Sum to 38:  {29}    {30}    {31}
         _  /  _  /  _  /
        / \/  / \/  / \/    {32}
       /   \ /   \ /   \    /        +-Space Map-+
      | {0}  | {1}  | {2}  |--/-----{19}  |   A B C   |
     / \   / \   / \   / \/    {33}    |  D E F G  |
    /   \ /   \ /   \ /   \    /     | H I J K L |
   | {3}  | {4}  | {5}  | {6}  |--/--{20}  |  M N O P  |
  / \   / \   / \   / \   / \/       |   Q R S   |
 /   \ /   \ /   \ /   \ /   \       +-----------+
| {7}  | {8}  | {9}  | {10}  | {11}  |--{21}
 \   / \   / \   / \   / \   /       +-----Z-----+
  \ /   \ /   \ /   \ /   \ /\       |{34} {35} {36} {37}|
   | {12}  | {13}  | {14}  | {15}  |--\--{22}  |{38} {39} {40} {41}|
    \   / \   / \   / \   /    \     |{42} {43} {44} {45}|
     \ /   \ /   \ /   \ /\    {24}    |{46} {47} {48} {49}|
      | {16}  | {17}  | {18}  |--\-----{23}  |{50} {51} {52}   |
       \   / \   / \   /    \        +-----------+
        \_/\  \_/\  \_/\    {25}
            \     \     \
            {28}    {27}    {26}"""

# The unused numbers box starts off with all integers 1 to 19:
unusedNums = set()
for i in range(1, 20):
    unusedNums.add(i)

# The hex board starts off with just blanks (that is, 0s)
board = {}
for space in 'ABCDEFGHIJKLMNOPQRS':
    board[space] = 0

while True: # Main game loop.
    rowSums = {} # The keys are row numbers, values are sums for that row.

    # ROW NUMBERING:
    #       12  14
    #    11 / 13/15
    #    / / / / /
    #   A B C-/-/--1
    #  D E F G-/---2
    # H I J K L----3
    #  M N O P-\---4
    #   Q R S-\-6--5
    #    \ \ \ 7
    #    10 9 8

    # Calculate the sum for each of the 15 rows:
    b = board # Syntactic sugar to have a shorter variable name.
    rowSums[1] = b['A'] + b['B'] + b['C']
    rowSums[2] = b['D'] + b['E'] + b['F'] + b['G']
    rowSums[3] = b['H'] + b['I'] + b['J'] + b['K'] + b['L']
    rowSums[4] = b['M'] + b['N'] + b['O'] + b['P']
    rowSums[5] = b['Q'] + b['R'] + b['S']
    rowSums[6] = b['C'] + b['G'] + b['L']
    rowSums[7] = b['B'] + b['F'] + b['K'] + b['P']
    rowSums[8] = b['A'] + b['E'] + b['J'] + b['O'] + b['S']
    rowSums[9] = b['D'] + b['I'] + b['N'] + b['R']
    rowSums[10] = b['H'] + b['M'] + b['Q']
    rowSums[11] = b['A'] + b['D'] + b['H']
    rowSums[12] = b['B'] + b['E'] + b['I'] + b['M']
    rowSums[13] = b['C'] + b['F'] + b['J'] + b['N'] + b['Q']
    rowSums[14] = b['G'] + b['K'] + b['O'] + b['R']
    rowSums[15] = b['L'] + b['P'] + b['S']

    # Prepare the arguments to use for the boardTemplate string:
    templateArgs = []

    # Indexes 0 to 18 of templateArgs are for the numbers 1 to 19:
    for space in 'ABCDEFGHIJKLMNOPQRS':
        if board[space] == 0:
            templateArgs.append('  ')
        else:
            templateArgs.append(str(board[space]).rjust(2))

    # Indexes 19 to 33 of templateArgs are for the row sums:
    for rowNumber in range(1, 16):
        templateArgs.append(str(rowSums[rowNumber]).rjust(2))

    # Indexes 34 to 52 of templateArgs are for the unused numbers box:
    for i in range(1, 20):
        if i in unusedNums:
            templateArgs.append(str(i).rjust(2))
        else:
            templateArgs.append('  ')

    # Display the hex board:
    print(boardTemplate.format(*templateArgs))

    # Quit the program if all rows add up to 38:
    isSolved = True
    for i in range(1, 16): # Loop over all 15 rows.
        if rowSums[i] != 38:
            isSolved = False # Unsolved if at least one row isn't 38.
    if isSolved:
        print('You\'ve solved the puzzle! Hurray!')
        break

    # Get the selected space from the user:
    while True:
        response = input('Select a space A to S (or Z or QUIT): ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if (response in 'ABCDEFGHIJKLMNOPQRS' + 'Z') and (response != ''):
            selectedSpace = response
            break

    # Get the selected number from the user to place on the selected space:
    while True:
        print('Enter a number 1 to 19 for', selectedSpace, '(or "quit"):')
        response = input()
        if response.lower().startswith('q'):
            print('Thanks for playing!')
            sys.exit()
        if response.isdecimal() and (1 <= int(response) <= 19):
            selectedNumber = int(response)
            break

    if selectedSpace == 'Z':
        # Move the number to the unused numbers box:
        unusedNums.add(selectedNumber)
        for space in 'ABCDEFGHIJKLMNOPQRS':
            if board[space] == selectedNumber:
                board[space] = 0 # Set this space to blank.

    elif selectedNumber in unusedNums:
        # Move the number from the unused numbers box to the board:
        numberAtOriginalSpace = board[selectedSpace]
        board[selectedSpace] = selectedNumber # Put the number on the board.
        unusedNums.remove(selectedNumber)
        if numberAtOriginalSpace != 0:
            unusedNums.add(numberAtOriginalSpace)
    else:
        # Since the number must already be on the board, do a swap to move
        # it to the selected space:
        for space in 'ABCDEFGHIJKLMNOPQRS':
            if board[space] == selectedNumber:
                spaceOfOriginalNumber = space

        numberAtOriginalSpace = board[selectedSpace]

        # Swap the two numbers on the board:
        board[selectedSpace] = selectedNumber
        board[spaceOfOriginalNumber] = numberAtOriginalSpace
