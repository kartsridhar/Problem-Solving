'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = str(input())
a, b, c = 0, 0, 0
for i in range(len(s)):
    if s[i] == 'a':
        a = 2*a + 1
    elif s[i] == 'b':
        b = 2*b + a
    elif s[i] == 'c':
        c = 2*c + b
print(c)