# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Creating groups of positive numbers whenever negative numbers occur
def splitAtNeg(A):
    new, group = [], []
    for i in A:
        if i < 0:
            if group:
                new.append(group)
                group = []
        else:
            group.append(i)
    if group:
        new.append(group)
    return new

def solution(A):
    # write your code in Python 3.6
    grouped = splitAtNeg(A)
    return -1 if len(grouped) == 0 else max([sum(i) for i in splitAtNeg(A)])
                    
