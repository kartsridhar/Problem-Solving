# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

N = int(input())
nums = list(map(float, input().split()))
print(np.mean(nums))
print(np.median(nums))
print(int(stats.mode(nums)[0]))