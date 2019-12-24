# Write your code here
"""
10 8
30 42
45 33
9 4
69 27
77 19
127 1
150 122
"""
def find_divisors(val):
    divisors = [i for i in range(1,val) if val%i == 0]
    return divisors
        
t = int(input())
for _ in range(t):
    val = int(input())
    print(sum(find_divisors(val)))