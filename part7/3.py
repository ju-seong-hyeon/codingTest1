def dfs(l, sum):
    global res
    if(l == n):
        if(0<sum<=s):
            res.add(sum)
    else:
        dfs(l+1, sum+a[l])
        dfs(l+1, sum-a[l])
        dfs(l+1, sum)

if __name__ == "__main__":
    n = 3
    a = [1, 5, 7]
    s = sum(a)
    res = set()
    dfs(0, 0)
    print(s - len(res))