# Progress Bar, by Al Sweigart al@inventwithpython.com
# A progress bar animation that can be used in other programs.

import random, time

def getProgressBar(progress, total, barWidth=40):
    """Returns a string that represents a progress bar that has `barWidth`
    bars and has progressed `progress` amount out of a `total` amount."""

    progressBar = '' # The progress bar will be a string value.
    progressBar += '[' # Create the left end of the progress bar.

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += '*' * numberOfBars # Add the progress bar.
    progressBar += ' ' * (barWidth - numberOfBars) # Add the empty space.
    progressBar += ']' # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%' # Add the percentage.

    progressBar += ' ' + str(progress) + '/' + str(total) # Add the numbers.

    return progressBar # Return the progress bar string.

# Simulate a download:
bytesDownloaded = 0
downloadSize = 4098
while bytesDownloaded < downloadSize:
    # "Download" a random amount of "bytes":
    bytesDownloaded += random.randint(0, 100)

    # Get the progress bar string for this amount of progress:
    barStr = getProgressBar(bytesDownloaded, downloadSize)

    # Don't print a newline at the end, and immediately flush the
    # printed string to the screen:
    print(barStr, end='', flush=True)

    # Pause for a little bit:
    time.sleep(0.2)

    # Print backspaces to erase the previously printed progress bar:
    print('\b' * len(barStr), end='', flush=True)
