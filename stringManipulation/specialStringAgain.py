#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    subs = []
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                subs.append(s[i:j+1]) 
    for k in range(len(subs)):
        if len(subs[k]) == 1:
            subs[k] = None
    res = [i for i in subs if i] 

    for r in res:
        if r[0] == r[-1] and r.count(r[0]) == len(r) - 1:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
