#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    s = list(s)
    openBrackets = ['(', '[', '{']
    closeBrackets = [')', ']', '}']
    stack = []

    if s[0] not in openBrackets:
        return "NO"

    for i in range(len(s)):
        if s[i] in openBrackets:
            stack.append(s[i])
        if s[i] in closeBrackets:
            bracketIndex = closeBrackets.index(s[i])
            if len(stack) != 0 and stack[-1] == openBrackets[bracketIndex]:
                stack.pop()
            else:
                return "NO"
                
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
