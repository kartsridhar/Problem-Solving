# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def stddev(n, arr, mean):
    return math.sqrt(sum((i-mean)**2 for i in arr)/n)

n = int(input())
arr = list(map(int, input().split()))
mean = sum(arr)/n
print(stddev(n, arr, mean))