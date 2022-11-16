def dfs(v, cur):
    global cnt
    if(v == m):
        for i in a:
            print(i, end = " ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if(cur != a[i]):
                a[v] = i
                dfs(v+1, cur+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    a = [0] * m
    ch = [0]
    dfs(0, 0)
    print(cnt)
