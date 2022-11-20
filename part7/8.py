from collections import deque
n = 5
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = [[10, 13, 10, 12, 15],
     [12, 39, 30, 23 ,11],
     [11, 25, 50, 53, 15],
     [19 ,27 ,29 ,37 ,27],
     [19, 13, 30, 13, 19]]
ch = [[False] * n for _ in range(n)]
dq = deque()
cur_x = 2
cur_y = 2
ch[cur_x][cur_y] = True
dq.append((cur_x, cur_y))
l = 0
cnt = 0
a_sum = arr[cur_x][cur_y]
while(dq):
    if(l==n//2):
        print(a_sum)
        break
    size = len(dq)
    for i in range(size):
        cur = dq.popleft()
        for i in range(4):
            cur_x = cur[0] + dx[i]
            cur_y = cur[1] + dy[i]
            if(ch[cur_x][cur_y] == False):
                dq.append((cur_x, cur_y))
                ch[cur_x][cur_y] =True
                a_sum += arr[cur_x][cur_y]
    l+=1
