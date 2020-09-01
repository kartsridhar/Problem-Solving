length = int(input())
arr = list(map(int, input().split()))

maxSum = 0
currentSum = 0
i = 0

while i < length:
    if arr[i] > 0:
        currentSum += arr[i]
        i += 1
    else:
        maxSum = max(maxSum, currentSum)
        currentSum = 0
        i += 2

print(maxSum)
