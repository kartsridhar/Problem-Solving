# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nCr(n, r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

per, num = map(int, input().split())
b = lambda x, n, p: nCr(n, x) * p**x * (1-p)**(n-x)
atmost = round(sum([b(i, num, per/100) for i in range(3)]), 3)
atleast = round(sum([b(i, num, per/100) for i in range(2, num+1)]), 3)
print(atmost)
print(atleast)