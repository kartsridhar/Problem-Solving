#!/bin/python3

import math
import os
import random
import re
import sys

def getFrequency(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def getUnique(s):
    unique = []
    for i in s:
        if i not in unique:
            unique.append(i)
    return unique

# Complete the isValid function below.
def isValid(s):
    freq = getFrequency(s)
    values = list(freq.values())
    uniqueVals = getUnique(values)
    if len(uniqueVals) == 1:
        return "YES"
    else:
        newFreq = getFrequency(values)
        newVals = list(newFreq.values())
        if len(newVals) == 2:
            if newVals[1] == 1:
                return "YES"
            else:
                return "NO"
        else: 
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
