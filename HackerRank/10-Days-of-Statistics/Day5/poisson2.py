# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(float, input().split())
print(round(160 + 40*(a + a**2), 3))
print(round(128 + 40*(b + b**2), 3))