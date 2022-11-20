from collections import deque

a = [[0,0,0,0,0,0,0],
     [0,1,1,1,1,1,0],
     [0,0,0,1,0,0,0],
     [1,1,0,1,0,1,1],
     [1,1,0,1,0,0,0],
     [1,0,0,0,1,0,0],
     [1,0,1,0,0,0,0]]
n = 7
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


dq = deque()
dq.append((0, 0))

while(dq):
    cur = dq.popleft()
    print(cur)
    if(cur[0] == n-1 and cur[1] == n-1):
        print(a[n-1][n-1])
        break
    for i in range(4):
        cur_x = cur[0] + dx[i]
        cur_y = cur[1] + dy[i]
        if(0<=cur_x< n and 0<=cur_y<n):
            if(a[cur_x][cur_y] == 0):
                a[cur_x][cur_y] = a[cur[0]][cur[1]] + 1
                dq.append((cur_x, cur_y))


