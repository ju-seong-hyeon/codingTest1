def dfs(v, m):
    global cnt

    if(v == m_cnt):
        if (m == n):
            cnt += 1
    else:
        for i in range(0, a[v][1] +1):
            dfs(v+1, m + (i * a[v][0]))



if __name__ == "__main__":
    n = 20
    m_cnt = 3
    a = [[5, 3], [10, 2], [1, 5]]
    cnt = 0
    dfs(0, 0)
    print(cnt)