'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
n = int(input())
nums = list(map(int, input().split()))
def func(num, nums, sol = []):
    combinations = []
    if num==1:
        if num not in sol:
            sol += [num]
            sol.sort()

            if num < 10 and sol not in combinations:
                combinations.append(sol)
    else:
        digits = list(range(1, min(num-nums+2, 10)))
        digits = list(set(nums).difference(sol))

        for i in digits:
            func(num-i, nums-1, sol+[i])
    return combinations

