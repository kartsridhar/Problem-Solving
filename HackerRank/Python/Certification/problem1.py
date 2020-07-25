#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#   eg: hello world ToY
#   result: HELLO WORLD tOy
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    sentenceList = sentence.split()
    resultList = []
    for word in sentenceList[::-1]:
        newWord = ""
        for char in word:
            if char.isupper():
                newWord += char.lower()
            else:
                newWord += char.upper()
        resultList.append(newWord)
    result = ' '.join(resultList)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
