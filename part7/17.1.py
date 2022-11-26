def dfs(lev, s):
    global res
    if(lev == m):
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 21450000
            for x in ch:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        res = min(res, sum)
    else:
        for i in range(s, len(pz)):
            ch[lev] = i
            dfs(lev+1, i+1)

if __name__ == "__main__":
    n = 4
    m = 4
    a = [[0 ,1 ,2 ,0],
         [1 ,0 ,2 ,1],
         [0 ,2 ,1 ,2],
         [2 ,0 ,1 ,2]]

    hs = []
    pz = []
    ch = [0] * m
    res = 21470000

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                hs.append((i, j))
            elif(a[i][j] == 2):
                pz.append((i, j))
    dfs(0, 0)
    print(res)