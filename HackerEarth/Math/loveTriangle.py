# Write your code here
from sys import stdin

def pattern(n):
    return n if n < 9 else (n%9 + 10*pattern(n//9))

lines = stdin.readlines()
for line in lines:
    print(pattern(int(line)))