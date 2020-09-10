#!/bin/python3

import math
import os
import random
import re
import sys

"""
N = 0
S = 1
W = 2
E = 3
"""

def findStartPos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] =='M':
                return (i,j)
def inRange(x,max_val):
    return 0 <= x < max_val

def isValid(x,y,matrix,visited):
    rangechk = inRange(x,len(matrix)) and inRange(y,len(matrix[0]))
    return 1 if rangechk and not visited[x][y] and matrix[x][y] != 'X' else 0
def countValidNodes(x,y,matrix,visited):
    val = 0
    val += isValid(x-1,y,matrix,visited)
    val += isValid(x+1,y,matrix,visited)
    val += isValid(x,y-1,matrix,visited)
    val += isValid(x,y+1,matrix,visited)
    return 1 if val > 1 else 0
#count no of times hermoine has to wave her wand
def no_of_waves(matrix):
    def helper(matrix,visited,curr_dir,pos,k):
        x,y = pos
        path = [(x,y,0)]
        visited[x][y] = True
        # path.append(pos)
        while path:
            x,y,val = path.pop(0)
            visited[x][y] = True
            if matrix[x][y] == '*':
                return val
            val += countValidNodes(x,y,matrix,visited)
            if isValid(x-1,y,matrix,visited):
                path.append((x-1,y,val))
            if isValid(x+1,y,matrix,visited):
                path.append((x+1,y,val))
            if isValid(x,y-1,matrix,visited):
                path.append((x,y-1,val)) 
            if isValid(x,y+1,matrix,visited):
                path.append((x,y+1,val)) 
    
    pos = findStartPos(matrix)
    visited = [[False for y in range(len(matrix[0]))] for x in range(len(matrix))]
    return helper(matrix,visited,0,pos,0)

# Complete the countLuck function below.
def countLuck(matrix, k):
    val = no_of_waves(matrix)
    return "Impressed" if val == k else "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()