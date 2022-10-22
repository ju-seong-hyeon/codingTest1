n = int(input())
cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    if(a[0] == a[1] and a[0] == a[2]):
        v = 10000 + a[0] * 1000
    elif(a[0] == a[1] and a[0] != a[2]):
        v = 1000 + a[0] * 100
    elif(a[1] == a[2] and a[1] != a[0]):
        v = 1000 + a[1] * 100
    else:
        v = max(a) * 100

    cnt = max(v, cnt)
print(cnt)