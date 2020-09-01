'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
num = list(map(int, list(input())))
dp = [None for _ in range(len(num))]
dp[0] = len([True for i in num if i % 2 == 0])

for i in range(1,len(num)):
    if num[i-1] % 2 != 0:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] - 1
print(*dp)