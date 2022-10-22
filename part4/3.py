n, m = map(int, input().split())
a = list(map(int, input().split()))

ll = 0
lr = sum(a)
a_min = lr
while(ll <= lr):
    mid = (ll + lr) // 2
    a_sum = 0
    cnt = 1

    for i in a:
        if(a_sum + i > mid):
            cnt += 1
            a_sum = i
        elif(a_sum == mid):
            cnt += 1
            a_sum = 0
        else:
            a_sum += i

    if(cnt == m):
        a_min = min(a_min, mid)
        lr = mid - 1
    elif(cnt < m):
        lr = mid - 1
    else:
        ll = mid + 1

print(a_min)