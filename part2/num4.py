n, m = map(int, input().split())
a = [0] * (n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        a[i+j] += 1

cnt = max(a)
for i, v in enumerate(a):
    if(cnt == v):
        print(i, end = " ")




