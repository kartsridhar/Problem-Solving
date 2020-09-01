#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.strip()
    rootL = math.sqrt(len(s))
    lo = int(rootL)
    up = math.ceil(rootL)
    splits = []
    for i in range(0,len(s),up):
        section = s[i:i+up]
        if len(section) != up:
            section += " " * (up - len(section))
        splits.append(section)
    result = ''
    for i in zip(*splits):
        result += ''.join(i).rstrip()
        result += " "
    
    return result.rstrip()
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
