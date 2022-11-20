def dfs(v, score, time):
    global a_max
    if(time > m):
        return
    if(v == n):
        a_max = max(score, a_max)
    else:
        dfs(v + 1, score + a[v][0], time + a[v][1])
        dfs(v + 1, score, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]
    a_max = 0
    dfs(0, 0, 0)
    print(a_max)