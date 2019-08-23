#!/bin/python3

def nextMove(posr, posc, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'd':
                dr = i
                dc = j
    netr = posr - dr
    netc = posc - dc
    if board[posr][posc] == 'd':
        print("CLEAN")
    elif netr != 0:
        if netr > 0:
            print("UP")
        else:
            print("DOWN")
    elif netc != 0:
        if netc > 0:
            print("LEFT")
        else:
            print("RIGHT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)