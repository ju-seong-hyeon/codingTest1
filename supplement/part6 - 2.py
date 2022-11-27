def dfs(lev):
    if(lev == n+1):
        for i in range(1, n+1):
            if(a[i] != 0):
                print(a[i], end = " ")
        print()
    else:
        a[lev] = lev
        dfs(lev + 1)
        a[lev] = 0
        dfs(lev + 1)

if __name__ == "__main__":
    n = 3
    a = [0] * (n+1)
    dfs(1)