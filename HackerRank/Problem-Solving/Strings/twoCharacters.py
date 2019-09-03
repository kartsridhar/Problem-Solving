#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    alpha = set(s)
    longest = 0
    for i in combinations(alpha, 2):
        separator = ""
        substring = separator.join(j for j in s if j in i)     
        if all(substring[k] != substring[k+1] for k in range(len(substring) - 1)):
            longest = max(longest, len(substring))
    return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
