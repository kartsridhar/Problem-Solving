#!/bin/python3

import math
import os
import random
import re
import sys

def getTop(arr, r, c):
    return [arr[r][c], arr[r][c+1], arr[r][c+2]]

def getBottom(arr, r, c):
    return [arr[r+2][c], arr[r+2][c+1], arr[r+2][c+2]]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for r in range(len(arr) - 2):
        for c in range(len(arr) - 2):
            hourglass = getTop(arr, r, c) + [arr[r+1][c+1]]+ getBottom(arr, r, c)
            total = sum(hourglass)
            sums.append(total)
    maximum = max(sums)
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
