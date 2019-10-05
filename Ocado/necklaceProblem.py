# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# You have a list where each number points to another.Find the length of the longest necklace
# A[0] = 5
# A[1] = 4
# A[2] = 3
# A[3] = 0
# A[4] = 1
# A[5] = 2

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    else:
        longest = 0         # to keep track of the longest chain
        for i in range(len(A)):
            length = 1      # shortest length of a chain will have 1 bead
            start = A[i]    # starting with the current index
            while A[start] != A[i]:
                length += 1     # incrementing the length until the start and end beads match
                start = A[start]
            if length > longest:    # if length longer than the longest, update
                longest = length
        return longest