def dfs(lev):
    global cnt
    if(lev == m):
        for i in b:
            print(i, end = " ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if(a[i] != 1):
                a[i] = 1
                b[lev] = i
                dfs(lev + 1)
                a[i] = 0

if __name__ == "__main__":
    n = 3
    m = 2
    cnt = 0
    a = [0] * (n+1)
    b = [0] * (m)
    cnt = 0
    dfs(0)
    print(cnt)