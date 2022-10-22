n, m = map(int, input().split())
a = []
for _ in range(n):
    k = int(input())
    a.append(k)

a.sort()
ll = 0
lr = a[-1]
a_max = 0
print(a)
while(ll<=lr):
    mid = (ll + lr) // 2
    cnt = 0
    for i in a:
        cnt += i//mid

    if(cnt == m):
        a_max = max(mid, a_max)
        ll = mid + 1
    elif(cnt < m):
        lr = mid - 1
    else:
        ll = mid + 1

print(a_max)