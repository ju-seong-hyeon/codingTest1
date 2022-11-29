def dfs(lev, s):
    global a_size
    cnt = 0
    if(lev == n):
        dis = 0

        for j in hm:
            val = 10000000
            for i in pz_c:
                val = min(val, (abs(i[0] - j[0]) + abs(i[1] - j[1])))
            dis += val
        # print(dis)
        a_size = min(a_size, dis)
            #print(val)
    else:

        for i in range(s, len_pz):
            pz_c[lev] = pz[i]
            dfs(lev + 1, i+1)



if __name__ == "__main__":
    n = 4
    m = 4
    a = [[0, 1, 2, 0],
         [1, 0, 2, 1],
         [0, 2, 1, 2],
         [2, 0, 1, 2]]
    pz = []
    hm = []
    pz_c = [0] * n
    for i in range(n):
        for j in range(n):
            if(a[i][j] == 1):
                hm.append((i,j))
            elif(a[i][j] == 2):
                pz.append((i,j))

    len_pz = len(pz)
    a_size = 10000000
    dfs(0, 0)
    print(a_size)
