#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    area = 0
    i = 0
    while i < len(h):
        if len(stack) == 0 or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if len(stack) == 0:
                area = max(area, h[top] * i)
            else:
                area = max(area, h[top] * (i - stack[-1] - 1))
    
    while len(stack) != 0:
        top = stack.pop()
        if len(stack) == 0:
            area = max(area, h[top] * i)
        else:
            area = max(area, h[top] * (i - stack[-1] - 1))
    
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
