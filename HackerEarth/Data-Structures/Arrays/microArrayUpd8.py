'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    _, val = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = val - min(arr)
    print(count if count>0 else 0)