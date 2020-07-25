#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'canReach' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def canReach(x1, y1, x2, y2):
    # Write your code here
    visited = []
    visited.append((x1, y1))
    flag = False

    while len(visited) != 0:
        curr = visited.pop(0)

        if curr[0] == x2 and curr[1] == y2:
            flag = True

        if curr[0] + curr[1] <= x2:
            visited.insert(0, (curr[0] + curr[1], curr[1]))

        if curr[0] + curr[1] <= y2:
            visited.insert(0, (curr[0], curr[0] + curr[1]))
    return "Yes" if flag else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    result = canReach(x1, y1, x2, y2)

    fptr.write(result + '\n')

    fptr.close()
