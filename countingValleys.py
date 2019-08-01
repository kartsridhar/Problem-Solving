#!/bin/python3

import math
import os
import random
import re
import sys

def getUnit(step):
    if step == 'U':
        return 1
    else:
        return -1       

# Complete the countingValleys function below.
def countingValleys(n, s):
    units = []
    for i in s:
        units.append(getUnit(i))
    seaLevel = 0
    valleyCount = 0
    for j in range(n):
        if units[j] == 1:
            seaLevel += 1
            if seaLevel == 0:
                valleyCount += 1
        else:
            seaLevel -= 1
    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
