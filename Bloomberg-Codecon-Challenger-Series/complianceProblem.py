#Problem        : A Compliance Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
from collections import Counter

data = sys.stdin.read().splitlines()

def isPalindrome(word):
    return word == word[::-1]

def canMakePalindrome(word):
    oddCharsCount = []
    for i in Counter(word).values():
        if i%2 != 0:
            oddCharsCount.append(i)
    return len(oddCharsCount) <= 1

word = data[0]

if isPalindrome(word) or canMakePalindrome(word):
    print("yes")
else:
    print("no")