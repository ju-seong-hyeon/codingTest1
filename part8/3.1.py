if __name__ == "__main__":
    n = 8
    a = [5, 3, 7, 8, 6, 2, 9, 4]
    a.insert(0, 0)
    res = [[0] * (n+1)]
    res[1] = 1
    for i in range(2, n+1):
