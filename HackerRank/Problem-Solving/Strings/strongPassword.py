#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    criteria = [False] * 4 # num = 0, lower = 1, upper = 2, special = 3
    for i in range(n):
        if password[i] in numbers:
            criteria[0] = True
        elif password[i] in lower_case:
            criteria[1] = True
        elif password[i] in upper_case:
            criteria[2] = True
        elif password[i] in special_characters:
            criteria[3] = True
    if not all(criteria):
        count = criteria.count(False)
        if len(password) + count < 6:
            count += 6 - (len(password) + count)
    else:
        if len(password) < 6:
            count = 6 - len(password)
            
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
