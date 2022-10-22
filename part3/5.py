n, m = map(int, input().split())
a = list(map(int, input().split()))

ll = 0
lr = 0
a_sum = 0
cnt = 0

while(1):
    if(a_sum < m):
        if(lr == len(a)):
            break
        a_sum += a[lr]
        lr += 1
    elif(a_sum == m):
        cnt += 1
        a_sum -= a[ll]
        ll += 1
    else:
        a_sum -= a[ll]
        ll += 1
    print(ll, lr, a_sum, cnt)

print(cnt)
