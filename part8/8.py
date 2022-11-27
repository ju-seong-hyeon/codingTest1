if __name__ == "__main__":
    n = 4
    m = 11
    a = [[5, 12], [3, 8], [6, 14], [4, 8]]
    res = [0] * (m+1)
    # 무게 , 가치
    for i in a:
        weight = i[0]
        value = i[1]
        for j in range(weight, m+1):
            res[j] = max(res[j], res[j-weight] + value)
    print(res[m])