def func(mid):
    cnt = 1
    cur = a[0]
    for i in range(1, n):
        if a[i] - cur >= mid:
            cnt += 1
            cur = a[i]
    return cnt

n = 5
m = 3
a = [1,2,8,4,9]
a.sort()

ll = a[0]
lr = a[-1]
res = 0
while(ll<=lr):
    mid = (ll + lr) // 2
    cnt = func(mid)
    if(cnt == m):
        res = max(res, mid)
        ll = mid + 1
    elif(cnt > m ):
        ll = mid + 1

    else:
        lr = mid - 1

print(res)