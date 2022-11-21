dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(x, y):
    global cnt
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0<=xx<n and 0<=yy<n):
            if(ch[xx][yy] == False):
                if(a[xx][yy] == 1):
                    a[xx][yy] = a_cnt
                    ch[xx][yy] = True
                    dfs(xx, yy)
                    cnt += 1

if __name__ == "__main__":
    # n = int(input())
    # a = [list(map(int, input())) for _ in range(n)]
    n = 7
    a = [[0,1,1,0,1,0,0],
         [0,1,1,0,1,0,1],
         [1,1,1,0,1,0,1],
         [0,0,0,0,1,1,1],
         [0,1,0,0,0,0,0],
         [0,1,1,1,1,1,0],
         [0,1,1,1,0,0,0]]
    ch = [[False] * n for _ in range(n)]
    res = []
    a_cnt = 1
    cnt = 0

    for i in range(n):
        for j in range(n):
            if(a[i][j] == 1 and ch[i][j] == False):
                dfs(i, j)
                a_cnt += 1
                res.append(cnt)
                cnt = 0

    print(len(res))
    res.sort()
    for i in res:
        print(i)
    