def func(a, mid):
    cur = a[0]
    a_dif = 0
    cnt = 1

    for i in range(1, n):
        if ((a[i] - cur) >= mid):
            a_dif = max(a[i] - cur, a_dif)
            cur = a[i]
            cnt += 1

    return cnt, a_dif

n, m = map(int, input().split())
a = []
for _ in range(n):
    v = int(input())
    a.append(v)
a.sort()
ll = a[0]
lr = a[-1]

while(ll <= lr):
    mid = (ll + lr) // 2
    cur = a[0]

    cnt, a_dif = func(a, mid)
    print(a_dif)
    if(cnt == m):
        a_dif = max(a_dif, mid)
        ll = mid + 1
    elif(cnt > m):
        ll = mid + 1
    else:
        lr = mid - 1

print(a_dif)



