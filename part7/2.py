def dfs(v, score):
    global a_max
    if(v == n):
        a_max = max(a_max, score)
    else:
        dfs(v+1, score)
        dfs(v+a[v][0], score+a[v][1])


if __name__ == "__main__":
    n = 7
    a = [[4, 20], [2, 10], [3, 15], [3, 20], [2,30], [2, 20], [1, 10]]
    a_max = 0
    dfs(0, 0)
    print(a_max)