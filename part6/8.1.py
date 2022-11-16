def dfs(v, cur):
    global cnt
    if(v == m):
        for i in a:
            print(i, end = " ")
        print()
        cnt += 1
    else:
        for i in range(cur, n+1):
            a[v] = i
            dfs(v+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    a = [0] * m
    dfs(0, 1)
    print(cnt)
