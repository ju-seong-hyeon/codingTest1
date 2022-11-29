def dfs(L, s):
    global res
    cnt = 0
    if(L == m):
        sum = 0
        cnt += 1
        #print(cb)
        for x in cb:
            x2 = pz[x][0]
            y2 = pz[x][1]
            print(x2, y2)
        # for j in range(len(hs)):
        #     x1 = hs[j][0]
        #     y1 = hs[j][1]
        #     dis = 214600000
        #     for x in cb:
        #         x2 = pz[x][0]
        #         y2 = pz[x][1]
        #         print(x2, y2)
        #         cnt += 1
        #         dis = min(dis, abs(x1 - x2) + abs(y1-y2))
        #     sum += dis
        # print(sum)
        # res = min(res, sum)
        #print(cnt)
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            dfs(L+1, i+1)

if __name__ == "__main__":
    n = 4
    m = 4
    a = [[0, 1, 2, 0],
         [1, 0, 2, 1],
         [0, 2, 1, 2],
         [2, 0, 1, 2]]
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                hs.append((i, j))
            elif a[i][j] == 2:
                pz.append((i, j))

    dfs(0, 0)
    print(res)