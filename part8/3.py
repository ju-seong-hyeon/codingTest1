if __name__ == "__main__":
    n = 8
    # a = [5,3,7,8,6,2,9,4]
    a = [5, 2, 18, 3, 4, 7, 10, 9, 11, 8, 15 ]
    a.insert(0, 0)
    res = [0] * (n+1)
    res[1] = 1
    a_max = a[1]
    cur = 1
    for i in range(2, n+1):
        if(a[i] > a_max):
            res[i] = res[cur] + 1
            cur = i
            a_max = a[i]
            print(a[i])
    print(res)
    print(max(res))

