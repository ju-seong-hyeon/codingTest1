n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ll = 0
lr = n-1

while(ll<=lr):
    mid = (ll + lr) // 2

    if(a[mid] == m):
        print(mid+1)
        break
    elif(a[mid] < m):
        ll = mid + 1
    else:
        lr = mid - 1

