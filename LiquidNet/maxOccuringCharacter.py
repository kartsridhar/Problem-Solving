#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter
#
# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

def maximumOccurringCharacter(text):
    # Write your code here
    counts = [0 for i in range(256)]

    maxCount = -1

    for i in text:
        counts[ord(i)] += 1
    
    output = ''
    for i in text:
        if maxCount < counts[ord(i)]:
            maxCount = counts[ord(i)]
            output = i
    
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = maximumOccurringCharacter(text)

    fptr.write(str(result) + '\n')

    fptr.close()
