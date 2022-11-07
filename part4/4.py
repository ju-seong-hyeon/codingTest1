n, m = map(int, input().split())
a = []
for _ in range(n):
    k = int(input())
    a.append(k)

a.sort()

ll = a[0]
lr = a[-1]
a_max = 0
a_dif = 0
while(ll<=lr):
    mid = (ll + lr) // 2
    cur = ll
    v = 1
    a_max = 0

    for i in range(1, n):
        if(cur - a[i] >= mid):
            if(cur - a[i] > a_dif):
                a_dif = cur - a[i]
            cur = a[i]
            v += 1


    if(v == m):
        a_max = max(a_dif, a_max)
        ll = mid + 1
    elif(v > m):
        ll = mid + 1
    else:
        lr = mid - 1

print(a_max)