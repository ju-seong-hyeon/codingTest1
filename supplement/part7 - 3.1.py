def dfs(lev, val):
    if lev == n:
        if(0<val<=a_sum):
            b_set.add(val)
    else:
        dfs(lev + 1, val + arr[lev])
        dfs(lev + 1, val - arr[lev])
        dfs(lev + 1, val)


if __name__ == "__main__":
    n = 3
    arr = [1, 5, 7]
    a_sum = sum(arr)
    b_set = set()
    dfs(0, 0)
    print(b_set)