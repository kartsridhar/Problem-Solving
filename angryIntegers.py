# count the number of angry numbers less than the current number
# angry number = an integer of the form a^x + b^y 
# upper bound = 100000

def computeAxBy(a, b):
    upperBound = 9223372036854775806
    result = []

    x = 1
    y = 1

    while x <= upperBound:
        while y <= upperBound:
            if x + y <= upperBound:
                result.append(x + y)
                y *= b
        
        x *= a
        y = 1

    return result

def countAngry(n, a, b, x):
    integers = computeAxBy(a, b)
    for i in range(n):
        print(sum(1 for j in integers if j < x[i]))

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    x = list(map(int, input().split()))
    countAngry(n, a, b, x)