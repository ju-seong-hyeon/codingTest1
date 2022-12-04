C = int(input())
for i in range(C):
    a = list(map(int, input().split()))
    a_sum = 0
    for i in range(1, a[0]+1):
        a_sum += a[i]
    avg = a_sum / a[0]
    cnt = 0
    # print(a)
    for i in range(1, a[0]+1):
        if(a[i] > avg):
            cnt += 1
    print("{:.3f}%".format(cnt / a[0] * 100))
