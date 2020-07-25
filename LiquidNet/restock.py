#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

def restock(itemCount, target):
    # Write your code here
    print(itemCount)
    length = len(itemCount)
    total = 0
    i = 0
    while i < length:
        if total >= target:
            break
        else:
            total += itemCount[i]
        i += 1
    return abs(target - total)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    itemCount_count = int(input().strip())

    itemCount = []

    for _ in range(itemCount_count):
        itemCount_item = int(input().strip())
        itemCount.append(itemCount_item)

    target = int(input().strip())

    result = restock(itemCount, target)

    fptr.write(str(result) + '\n')

    fptr.close()
