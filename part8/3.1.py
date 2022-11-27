if __name__ == "__main__":
    n = 8
    a = [5, 3, 7, 8, 6, 2, 9, 4]
    a.insert(0, 0)
    res = [0] * (n+1)
    res[1] = 1
    for i in range(2, n+1):
        a_max = 0
        for j in range(i-1, 0, -1):
            if(a[j] < a[i] and res[j] > a_max):
                a_max = res[j]
        res[i] = a_max + 1
    print(res)
    print(max(res))


