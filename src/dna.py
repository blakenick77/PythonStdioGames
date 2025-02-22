# DNA Animation Demo by Al Sweigart
# A simple animation of a DNA double-helix.

# Thanks to matoken for inspiration: https://asciinema.org/a/155441

import random, time

# These are the individual rows of the DNA animation:
rows = [
    '         ##', # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',    # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

print('Press Ctrl-C to quit...')
time.sleep(2)
rowIndex = 0

try:
    while True: # Main animation loop.
        # Increment rowIndex to draw next row:
        rowIndex += 1
        if rowIndex == len(rows):
            rowIndex = 0

        # Row indexs 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(rows[rowIndex])
            continue

        # Select random nucleotide pairs:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # Print the row.
        print(rows[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(0.15) # Add a slight pause.
except KeyboardInterrupt:
    pass # Make the program stop looping.