if __name__ == "__main__":
    # n = 3
    # a = [1, 2, 5]
    # v = 15
    n = 5
    a = [1,5,7, 11,15]
    v = 39
    res = [v] * (v+1)
    res[0] = 0
    for i in a:
        money = i
        for j in range(money, v+1):
            #print(res[j-money] + money)
            res[j] = min(res[j], res[j - money] + 1)

    print(res[v])