'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here (ATTEMPT 2)
n = int(input())
arr = list(map(int, input().split()))
flag = False
for _ in range(n):
    val = arr.pop(0)
    for j in arr:
        if j > val:
            flag = True
            break
    if flag == False:
        print(val, end=" ")
    flag = False

