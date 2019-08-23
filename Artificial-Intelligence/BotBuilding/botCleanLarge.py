

def next_move(posx, posy, dimx, dimy, board):
    dist = []
    dirts = []
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                dx = i
                dy = j
                dirts.append([dx, dy])
                d1 = (posx - dx) ** 2
                d2 = (posy - dy) ** 2
                dist.append((d1 + d2) ** 1/2)
    nearest = min(dist)
    idx = dist.index(nearest)
    nx = dirts[idx][0]
    ny = dirts[idx][1]

    netx = posx - nx
    nety = posy - ny

    if board[posx][posy] == 'd':
        print("CLEAN")
    elif netx != 0:
        if netx > 0:
            print("UP")
        else:
            print("DOWN")
    elif nety != 0:
        if nety > 0:
            print("LEFT")
        else:
            print("RIGHT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)