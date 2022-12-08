n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    arr = list(map(int, input().split()))
    a.append(arr)

for i in range(n):
    brr = list(map(int, input().split()))
    b.append(brr)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = " ")
    print()