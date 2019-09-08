'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from collections import Counter
# Write your code here
n = int(input())
nums = list(map(int, input().split()))
q = int(input())
counts = Counter(nums)
for i in range(q):
    b = int(input())
    print(counts[b] if counts[b] else "NOT PRESENT")