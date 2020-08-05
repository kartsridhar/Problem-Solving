#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    minVal = 2*(10**9)
    arr.sort()
    for i in range(1,len(arr)):
        if abs(arr[i] - arr[i-1]) <= minVal:
            minVal = abs(arr[i] - arr[i-1])
    return minVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
