def dfs(v):
    global cnt
    if(v == m):
        for i in range(0, m):
            print(a[i], end = " ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            a[v] = i
            dfs(v+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)