import random
import sys
import time

"""get_choice
Gets input from a user but only accepts the given acceptable choices.

Keyword arguments:
message -- the prompt to print for the user
which -- the valid choices
whichRep -- how to express the valid choices to the users 
inputFunction - function to call to get input from user
verify - how to validate user input
"""


def get_choice(message, which, whichRep, inputFunction=input, verifyFunction=None):
    def verify(retVal, choices):
        if retVal not in choices:
            print('ERROR: invalid choice--enter ' + whichRep)
            input('Please press enter...')
            return False
        return True

    if verifyFunction == None:
        verifyFunction = verify

    hold = []
    for each in which:
        try:
            hold.append(str(each))
        except ValueError as err:
            print(err)

    ret = inputFunction(message)

    while not verifyFunction(ret, hold) or ret == '':
        ret = inputFunction(message)
    return ret


"""fake_loading_bars
Procedurally print a loading bar, just for funsies.

Keyword arguments:
low -- the lowest time to 'load' in seconds
high -- the highest time to 'load' in seconds
lineLength -- the length of the line
sleep -- thelength of time to sleep between each print
activities -- the list of things to 'load'
"""


def fake_loading_bars(low, high, lineLength, sleep, *activities):
    print('-' * lineLength)
    for k in activities:
        if k[len(k) - 1] != ' ':
            k += ' '
        print(k, end='')
        length = lineLength - len(k)
        sys.stdout.flush()
        timing = random.randint(low, high)
        for _ in range(lineLength - len(k)):
            time.sleep(timing / length)
            print('\u25A0', end='')
            sys.stdout.flush()
        time.sleep(sleep)
        print()
    print('-' * lineLength)
