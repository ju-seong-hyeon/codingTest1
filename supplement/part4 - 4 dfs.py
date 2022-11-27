def dfs(lev, s):
    global a_max
    if(lev == m):
        for i in range(1, m):
            a_max = max(abs(arr[i] - arr[i-1]), a_max)
        print(a_max)
        print(arr)

    else:
        for i in range(s, n):
            arr[lev] = a[i]
            dfs(lev+1, i+1)


if __name__ == "__main__":
    n = 5
    m = 3
    a = [1,2,8,4,9]
    a.sort()
    arr = [0] * m
    a_max = 0
    dfs(0, 0)
    print(a_max)