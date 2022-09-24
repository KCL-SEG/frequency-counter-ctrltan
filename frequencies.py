"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range (0,len(items)):
        if isinstance(items[i], int) == True:
            items[i] = f'{items[i]}'
            if items[i] not in frequencies.keys():
                frequencies[items[i]] = 1
            else:
                frequencies[items[i]] += 1
        else:
            if items[i] not in frequencies.keys():
                frequencies[items[i]] = 1
            else:
                frequencies[items[i]] += 1

    return frequencies
