n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    a[i].append(0)
    a[i].insert(0, 0)

b = [0,0,0,0,0,0,0]
a.insert(0, b)
a.append(b)
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if(a[i][j] > max(a[i-1][j], a[i+1][j], a[i][j-1], a[i][j+1])):
            cnt += 1

print(cnt)