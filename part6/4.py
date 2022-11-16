def dfs(v, a_max):
    global a_ret
    if(a_max >= n):
        return
    if(v == m):
        a_ret = max(a_max, a_ret)
        return
    else:
        dfs(v+1, a_max+a[v])
        dfs(v+1, a_max)

if __name__ == "__main__":
    # n, m = map(int, input().split())
    # a = []
    # for _ in range(m):
    #     v = int(input())
    #     a.append(v)
    n = 259
    m = 5
    a = [81, 58, 42, 33, 61]
    a_ret = 0
    dfs(0, 0)
    print(a_ret)