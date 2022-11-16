def dfs(l):
    global cnt
    if (l == m):
        for i in range(m):
            print(res[i], end = " ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                dfs(l+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    dfs(0)
    print(cnt)