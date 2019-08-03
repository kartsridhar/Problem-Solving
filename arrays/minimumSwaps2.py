#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    flag = [False] * len(arr)
    swapCount = 0

    for i in range(len(arr)):
        j = i
        rounds = 0

        while (not flag[j]):
            flag[j] = True
            j = arr[j] - 1
            rounds += 1

        if rounds is not 0:
            swapCount += rounds - 1
    return swapCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
