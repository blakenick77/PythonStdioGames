# 99 Bottles of Beer on the Wall, by Al Sweigart al@inventwithpython.com

import time

print('NINETY NINE BOTTLES OF BEER')
print('By Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')
print()

time.sleep(2)

bottles = 99 # This is the starting number of bottles.
PAUSE = 1 # A constant that sets how many seconds each pause is.

while bottles > 1: # Keep looping and display the lyrics.
    print(bottles, 'of beer on the wall,')
    time.sleep(PAUSE) # Pause for PAUSE number of seconds.
    print(bottles, 'bottles of beer,')
    time.sleep(PAUSE)
    print('Take one down, pass it around,')
    time.sleep(PAUSE)
    bottles = bottles - 1 # Decrease the number of bottles by one.
    print(bottles, 'bottles of beer on the wall!')
    time.sleep(PAUSE)
    print()

# Display the last stanza:
print('1 bottle of beer on the wall,')
time.sleep(PAUSE)
print('1 bottle of beer,')
time.sleep(PAUSE)
print('Take it down, pass it around,')
time.sleep(PAUSE)
print('No more bottles of beer on the wall!')
