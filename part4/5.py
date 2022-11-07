n = int(input())
a = []
for _ in range(n):
    i, j = map(int, input().split())
    a.append((i, j))

a.sort(key = lambda x : (x[1], x[0]))
print(a)
cnt = 1
cur = a[0][1]
for i in range(1, n):
    if(cur - a[i][0] <= 0):
        cur = a[i][1]
        cnt += 1

print(cnt)
