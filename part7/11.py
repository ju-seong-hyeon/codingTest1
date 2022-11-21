dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt
    if(x == a_max_x and y == a_max_y):
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0<=xx<n and 0<=yy<n):
                if(a[xx][yy] > a[x][y]):
                    dfs(xx, yy)


if __name__ == "__main__":
    n = 5
    a = [[2,23,92,78,93],
         [59,50,48,90,80],
         [30,53,70,75,96],
         [94,91,82,89,93],
         [97,98,95,96,100]]

    MAX = 100
    MIN = 0
    a_min_x = 0
    a_min_y = 0
    a_max_x = 0
    a_max_y = 0
    a_min = MAX + 1
    a_max = MIN - 1


    for i in range(n):
        for j in range(n):
            if(a_min > a[i][j]):
                a_min = a[i][j]
                a_min_x = i
                a_min_y = j

            if(a_max < a[i][j]):
                a_max = a[i][j]
                a_max_x = i
                a_max_y = j
    #
    # print(a_max, a_max_x, a_max_y)
    # print(a_min, a_min_x, a_min_y)

    ch = [[False] * n for _ in range(n)]
    ch[a_min_x][a_min_y] = True
    cnt = 0
    dfs(a_min_x, a_min_y)
    print(cnt)


