#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
            continue
        i += 1
    if len(s) == 0:
        return "Empty String"
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
