# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

mu = float(input())
rv = int(input())
p = lambda l, k : ((l**k) * (1/math.exp(l)))/math.factorial(k)
print(round((p(mu, rv)), 3))