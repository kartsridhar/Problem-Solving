# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

maxWt = float(input())
n = float(input())
mean = float(input())
std = float(input())
mean *= n
std  = std * math.sqrt(n)
phi = lambda m, v, val : 0.5 * (1+math.erf((val-m)/(v*math.sqrt(2))))

print(round(phi(mean, std, maxWt), 4))