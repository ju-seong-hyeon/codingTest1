def dfs(lev, a, b, c):
    if(lev == n):

    else:
        dfs(lev + 1, a + arr[lev], b, c)
        dfs(lev + 1, a, b + arr[lev], c)
        dfs(lev + 1, a, b, c + arr[lev])

if __name__ == "__main__":
    n = 3
    arr = [1, 5, 7]
    a_sum = sum(arr)
    res = [0] * a_sum
    brr = set()
    dfs(0, 0, 0, 0)
    print(brr)