def dfs(a_sum, a_cnt):
    global cnt
    if (cnt < a_cnt):
        return
    if(a_sum == m):
        cnt = min(cnt, a_cnt)
    elif(a_sum > m):
        return
    else:
        for i in a:
            dfs(a_sum + i, a_cnt + 1)


if __name__ == "__main__":
    n = 3
    a = [1,2,5]
    m = 15
    a.sort(reverse = True)
    cnt = a[-1] * m
    dfs(0, 0)
    print(cnt)
