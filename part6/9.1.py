def dfs(v, cur, a_sum):
    global cnt
    if(v == m):
        if(a_sum % val == 0):
            cnt += 1
    else:
        for i in range(cur, n):
            dfs(v+1, i+1, a_sum + a[i])


if __name__ == "__main__":
    n = 5
    m = 3
    a = [2, 4, 5, 8, 12]
    cnt = 0
    val = 6
    dfs(0, 0, 0)
    print(cnt)