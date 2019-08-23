#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    subs = []
    for i in range(n):
        for j in range(1, n-i+1):
            if s[i:i+j][0] == s[i:i+j][-1]:
                subs.append(s[i:i+j])
                count += 1
    for x in range(len(subs)):
        if not all(y == subs[x][0] for y in subs[x]) and subs[x].count(subs[x][0]) != len(subs[x]) - 1:
            subs[x] = None
    subs = [i for i in subs if i] 
    return len(subs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
