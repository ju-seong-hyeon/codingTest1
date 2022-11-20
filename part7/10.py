dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt
    print(x, y)
    if(x == n-1 and y == n-1):
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0<=xx<n and 0<=yy<n):
                if(a[xx][yy] == 0):
                    a[xx][yy] = 1
                    dfs(xx, yy)
                    a[xx][yy] = 0

if __name__ == "__main__":
    n = 7
    a = [[0,0,0,0,0,0,0],
         [0,1,1,1,1,1,0],
         [0,0,0,1,0,0,0],
         [1,1,0,1,0,1,1],
         [1,1,0,0,0,0,1],
         [1,1,0,1,1,0,0],
         [1,0,0,0,0,0,0]]
    cnt = 0
    a[0][0] = 1
    dfs(0, 0)
    print(cnt)
