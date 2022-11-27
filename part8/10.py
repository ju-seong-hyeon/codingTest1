if __name__ == "__main__":
    n = 5
    m = 20
    a = [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]
    # 점수, 시간
    res = [0] * (m + 1)

    for i in a:
        score = i[0]
        time = i[1]
        for j in range(time, m+1):
            res[j] = max(res[j], res[j - time] + score)

    print(res[m])