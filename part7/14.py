dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(x, y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0<=xx<n and 0<=yy<n):
            if(a[xx][yy] > 0):
                if(ch[xx][yy] == False):
                    ch[xx][yy] = True
                    dfs(xx, yy)

if __name__ == "__main__":
    n = 5
    a = [[6,8,2,6,2],
         [3,2,3,4,6],
         [6,7,3,3,2],
         [7,2,5,3,6],
         [8,9,5,2,7]]
    a_max = max(map(max, a))
    a_min = min(map(min, a))

    for i in range(n):
        for j in range(n):
            a[i][j] -= a_min
    a_max_v = 0

    for k in range(1, a_max):
        ch = [[False] * n for _ in range(n)]
        a_cnt = 0
        for i in range(n):
            for j in range(n):
                if(a[i][j] > 0 and ch[i][j] == False):
                    dfs(i, j)
                    a_cnt += 1
        a_max_v = max(a_max_v, a_cnt)
        for i in range(n):
            for j in range(n):
                a[i][j] -= 1

    print(a_max_v)


