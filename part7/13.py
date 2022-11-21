dx = [-1, 0, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 1, 0, 1, -1, 0, 1]

def dfs(x, y):
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0<=xx<n and 0<=yy<n):
            if(ch[xx][yy] == False):
                if(a[xx][yy] == 1 ):
                    a[xx][yy] = 0
                    ch[xx][yy] = True
                    dfs(xx, yy)


if __name__== "__main__":
    n = 7
    a = [[1,1,0,0,0,1,0],
         [0,1,1,0,1,1,0],
         [0,1,0,0,0,0,0],
         [0,0,0,1,0,1,1],
         [1,1,0,1,1,0,0],
         [1,0,0,0,1,0,0],
         [1,0,1,0,1,0,0]]
    ch = [[False] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if(a[i][j] == 1):
                dfs(i, j)
                cnt += 1
    print(cnt)