'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
arr = list(map(int, input().split()))
x, y = [], []
for i in range(n):
    xtemp = -1
    for j in range(i):
        if arr[j] > arr[i]:
            xtemp = j+1
    x.append(xtemp)
    ytemp = -1
    for k in range(i, n):
        if arr[k] > arr[i]:
            ytemp = k+1
            break
    y.append(ytemp)
for a, b in zip(x, y):
    print(a+b, end=" ")
print("")