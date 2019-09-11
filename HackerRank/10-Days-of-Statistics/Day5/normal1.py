# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
m, v = map(float, input().split())
less = float(input())
s, e = map(float, input().split())
phi = lambda mean, std, val : 0.5 * (1+math.erf((val-mean)/(std*math.sqrt(2))))
print(round(phi(m, v, less), 3))
print(round(phi(m, v, e) - phi(m, v, s), 3))