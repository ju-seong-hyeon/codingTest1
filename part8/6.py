if __name__ == "__main__":
    n = 5
    a = [[3,7,2,1,9],
         [5,8,3,9,2],
         [5,3,1,2,3],
         [5,4,3,2,1],
         [1,7,5,2,4]]

    res = [[0] * n for _ in range(n)]
    res[0][0] = a[0][0]
    for i in range(1, n):
        res[i][0] = res[i-1][0] + a[i][0]
        res[0][i] = res[0][i-1] + a[0][i]
    print(res)

    for i in range(1, n):
        for j in range(1, n):
            res[i][j] = min(res[i-1][j], res[i][j-1]) + a[i][j]
    print(res)
    print(res[n-1][n-1])