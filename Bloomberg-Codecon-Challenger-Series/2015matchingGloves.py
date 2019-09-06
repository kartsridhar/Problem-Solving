#Problem        : Finals Spring 2015 - Matching Gloves
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT
from collections import Counter

n = int(input())

def isPalindrome(s):
    return s == s[::-1]

words = [str(input()) for _ in range(n)]
pairs, pali = 0, 0
cnt = Counter(words)

for i, j in cnt.items():
    if isPalindrome(i):
        pali += 1
        continue
    if i[::-1] in cnt:
        if cnt[i] == cnt[i[::-1]]:
            pairs += j/2

if 2 * int(pairs) + int(pali) == len(words):
    print(int(pairs))
else:
    print(-1)