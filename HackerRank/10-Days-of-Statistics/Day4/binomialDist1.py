# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nCr(n, r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

boy, girl = map(float, input().split())
ratio = boy/girl
b = lambda x, n, p: nCr(n, x) * p**x * (1-p)**(n-x)
print(round(sum([b(i, 6, ratio/(1+ratio)) for i in range(3,7)]), 3))