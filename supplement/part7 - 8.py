from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = 5
a = [[10, 13, 10, 12,15],
     [12, 39, 30, 23, 11],
     [11, 25, 50, 53, 15],
     [19, 27, 29, 37, 27],
     [19, 13, 30 , 13, 19]]
ch = [[0] * n for _ in range(n)]
dq = deque()
dq.append((n//2, n//2))
cnt = 0
a_sum = a[n//2][n//2]

while(dq):
    cnt += 1
    cur = dq.popleft()
    print(cur)
    size = len(dq)
    for i in range(size):
    for i in range(4):
        x = cur[0] + i
        y = cur[1] + i
        if(0<=x<n and 0<=y<n):
            if(ch[x][y] == 0):
                ch[x][y] = 1
                a_sum += a[x][y]
                dq.append((x, y))

    if(cnt == (n//2 + 12)):
        print(a_sum)
        break

