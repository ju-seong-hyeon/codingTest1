def dfs(v, cur, a_val):
    global cnt
    if(v == m):
        if(a_val % k == 0):
            cnt += 1
    else:
        for i in range(cur, n):
            dfs(v+1, i+1, a_val + a[i])


if __name__ == "__main__":
    n = 5
    m = 3
    a =[2, 4, 5, 8, 12]
    k = 6
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)