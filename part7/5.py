def dfs(v, a, b, c):
    global a_dif
    if(v == n):
        if(a != b and b != c and a != c):
            a_max = max(a, b, c)
            a_min = min(a, b, c)
            a_dif = min(a_max - a_min, a_dif)
            print(a, b, c, a_dif)
    else:
        dfs(v+1, a+arr[v], b, c)
        dfs(v+1, a, b+arr[v], c)
        dfs(v+1, a, b, c+arr[v])

if __name__ == "__main__":
    n = 7
    arr = [8, 9, 11, 12, 23, 15, 17]
    a_dif = sum(arr)
    dfs(0, 0, 0, 0)
    print(a_dif)