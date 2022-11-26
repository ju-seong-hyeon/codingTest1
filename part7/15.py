from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

if __name__ == "__main__":
    y = 6
    x = 4
    a = [[0,0,-1,0,0,0],
         [0,0,1,0,-1,0],
         [0,0,-1,0,0,0],
         [0,0,0,0,-1,1]]
    dq = deque()
    for i in range(x):
        for j in range(y):
            if(a[i][j]) == 1:
                dq.append((i, j))
                a[i][j] = 0

    while(dq):
        cur = dq.popleft()
        for i in range(4):
            xx = cur[0] + dx[i]
            yy = cur[1] + dy[i]
            if(0<=xx<x and 0<=yy<y):
                if(a[xx][yy] == 0):
                    a[xx][yy] = a[cur[0]][cur[1]] + 1
                    dq.append((xx, yy))

    print(max(map(max, a)))
