#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    nums = [0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty']
    
    for i in range(1,10):
        nums.append(f'twenty {nums[i]}')
    nums.append('half')

    hourWord = nums[h] if m < 31 else nums[h+1 % 12]
    
    result = ""

    if m == 0:
        result = hourWord + " o\' clock"
    elif m in range(1,31):
        if m == 1:
            inner = " minute past "
        elif m in [15,30]:
            inner = " past "
        else:
            inner = " minutes past "
        result = nums[m] + inner + hourWord 
    else:
        if m == 59:
            inner = " minute to "
        elif m == 45:
            inner = " to "
        else:
            inner = " minutes to "
        result = nums[60 % m] + inner + hourWord 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
