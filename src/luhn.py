# Luhn Checksum Algorithm, by Al Sweigart al@inventwithpython.com
# More info at: https://en.wikipedia.org/wiki/Luhn_algorithm
# More info at: https://youtu.be/Erp8IAUouus

import time, sys

PAUSE_AMOUNT = 0.5 # Pause for 0.5 seconds at each step.

print('''LUHN ALGORITHM
By Al Sweigart al@inventwithpython.com
''')

# Display information about the Luhn algorithm if the user wants it:
print('Would you like to see a description of the Luhn algorithm? Y/N')
if input().upper().startswith('Y'):
    print('''The Luhn algorithm is a checksum algorithm to make sure a serial number is
correct. It's used by credit cards and other official numbers.
More info at: https://en.wikipedia.org/wiki/Luhn_algorithm

For example, let's check the checksum for the number:
    79927398713
1) Get the non-checksum digits (every digit but the last).
    7992739871
2) From right to left, double every other digit.
    7 18 9 4 7 6 9 16 7 2
3) If a number is greater than 9, subtract 9.
    7 9 9 4 7 6 9 7 7 2
4) Add up all the numbers.
    7 9 9 4 7 6 9 7 7 2 = 67
5) Multiply by 9.
    67 * 9 = 603
6) The checksum digit is the last digit.
    60[3]
7) Append the checksum digit for the complete, valid number.
    79927398713

79927398713 has a valid Luhn checksum.
''')
    input('Press Enter to continue...') # Pause to let the user press Enter.


while True: # Main application loop.
    print('Enter a number to check its checksum (or QUIT):')
    originalNumber = input()

    if originalNumber.upper().startswith('Q'):
        sys.exit() # A response that begins with 'q' will quit the program.

    if not originalNumber.isdecimal():
        print('Please enter a number.')
        continue
    if len(originalNumber) < 2:
        print('The number must have at least two digits.')
        continue

    # Display each step of the Luhn algorithm:
    print('1) Get the non-checksum digits (every digit but the last):')
    nonChecksumDigits = list(originalNumber)[:-1]
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(PAUSE_AMOUNT)

    print('2) From right to left, double every other digit:')
    for i in range(len(nonChecksumDigits) - 1, -1, -2):
        nonChecksumDigits[i] = str(int(nonChecksumDigits[i]) * 2)
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(PAUSE_AMOUNT)

    print('3) If a number is greater than 9, subtract 9:')
    for i, number in enumerate(nonChecksumDigits):
        if int(number) > 9:
            nonChecksumDigits[i] = str(int(number) - 9)
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(PAUSE_AMOUNT)

    print('4) Add up all the numbers:')
    print('    ', end='')
    for i, number in enumerate(nonChecksumDigits):
        print(number, end=' ')
        nonChecksumDigits[i] = int(number) # Convert str to int.
    digitSum = sum(nonChecksumDigits)
    print('=', digitSum)
    time.sleep(PAUSE_AMOUNT)

    print('5) Multiply by 9:')
    digitSumTimesNine = digitSum * 9
    print(f'    {digitSum} * 9 = {digitSumTimesNine}')
    time.sleep(PAUSE_AMOUNT)

    print('6) The checksum digit is the last digit:')
    checksumDigit = str(digitSumTimesNine)[-1]
    print(f'    {str(digitSumTimesNine)[:-1]}[{checksumDigit}]')
    time.sleep(PAUSE_AMOUNT)

    print('7) Append the checksum digit for the complete, valid number:')
    numberWithValidChecksum = originalNumber[:-1] + str(checksumDigit)
    print(f'    {numberWithValidChecksum}')
    print() # Print a newline.
    time.sleep(PAUSE_AMOUNT)

    # Tell the user if they entered a valid number or not:
    if numberWithValidChecksum == originalNumber:
        print('You entered a VALID NUMBER.')
    else:
        print('You entered a number with an INVALID CHECKSUM.')
        print(f'The checksum should be {checksumDigit} not {originalNumber[-1]}')

    input('Press Enter to continue...')
    print() # Print some newlines for space.
    print()
    print()
