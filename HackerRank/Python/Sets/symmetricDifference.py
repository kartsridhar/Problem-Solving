# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
arr1 = set(map(int, input().split()))
N = int(input())
arr2 = set(map(int, input().split()))
result = list(arr1.symmetric_difference(arr2))
result.sort()
for i in result:
    print(i)
