# Eeny, Meeny, Miny, Moe, by Al Sweigart al@inventwithpython.com
# An elimination game for multiple players.

# More info at https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe
# More info at https://en.wikipedia.org/wiki/Josephus_problem

import random, time, sys

SCREEN_WIDTH = 60
RHYME = ['EENY', 'MEENY', 'MINY', 'MOE', 'CATCH A', 'TIGER', 'BY THE', 'TOE', 'IF IT', 'HOLLERS', 'LET IT', 'GO', 'EENY', 'MEENY', 'MINY', 'MOE']
NAMES = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer', 'Maria', 'Susan']
random.shuffle(NAMES)

print('Eeny, Meeny, Miny, Moe')
print('By Al Sweigart al@inventwithpython.com')
print()

# Get the players' names:
playerNames = []
while True:
    print('Enter a player\'s name, or enter nothing when finished:')
    playerName = input().upper()
    if playerName != '': # Player can enter anything except a blank name.
        playerNames.append(playerName)
    else:
        break

# Get the total number of participants:
while True:
    print('How many participants total (2-' + str(len(NAMES) + len(playerNames)) + '):')
    try:
        numParticipants = int(input())
    except ValueError:
        continue # Player entered non-integer; ask again.
    if 2 <= numParticipants <= len(NAMES) + len(playerNames):
        break

# Get the position of the player:
participants = NAMES[:numParticipants - len(playerNames)] # Get the required number of names.
for playerName in playerNames:
    while True:
        print('Where does ' + playerName + ' go? (1-' + str(len(participants) + 1) + '):')
        try:
            position = int(input())
        except ValueError:
            continue # Player entered non-integer; ask again.
        if 1 <= position <= len(participants) + 1:
            participants.insert(position - 1, playerName)
            break

# Start the elimination process:
startingPosition = 0
while len(participants) > 1:
    # Figure out how many names to put on each row:
    rows = ['']
    for name in participants:
        if len(rows[-1]) + len(name) > SCREEN_WIDTH:
            # Start a new row:
            rows.append('')

        rows[-1] += name + ' '

    # Run through one round of elimination:
    for rhymeWordIndex, rhymeWord in enumerate(RHYME):
        currentPerson = participants[(rhymeWordIndex + startingPosition) % len(participants)]
        for row in rows:
            # Include a space at the end, so we don't match names with the
            # same prefix, i.e. 'Doug' and 'Douglas':
            if currentPerson + ' ' in row:
                print(' ' * row.index(currentPerson) + rhymeWord)
            else:
                print()
            print(row)
        print('\n')
        time.sleep(0.5)
    startingPosition = (rhymeWordIndex + startingPosition) % len(participants)

    # Remove the eliminated person from the participants list:
    print(currentPerson.upper() + ' HAS BEEN ELIMINATED.')
    participants.remove(currentPerson)
    if currentPerson in playerNames:
        # If it's a player, remove them from playerNames:
        playerNames.remove(currentPerson)

    # If all players have been eliminated, end the game:
    if len(playerNames) == 0:
        print('ALL PLAYERS HAVE BEEN ELIMINATED.')
        print()
        print('Thanks for playing!')
        sys.exit()

    # Pause before starting the next elimination round.
    try:
        input('Press Enter to continue, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        # Player pressed Ctrl-C, so end the game.
        sys.exit()

# Declare the winner:
print(participants[0] + ' IS THE WINNER!!!')
