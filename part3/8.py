n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

q = int(input())
for _ in range(q):
    w, e, r = map(int, input().split())
    for _ in range(r):
        if(e == 0):
            a[w-1].append(a[w-1].pop(0))
        else:
            a[w-1].insert(0, a[w-1].pop())

ll = 0
lr = n
a_sum = 0

for i in range(0, n):
    for j in range(ll, lr):
        a_sum += a[i][j]
    if(i < n//2):
        ll += 1
        lr -= 1
    else:
        ll -= 1
        lr += 1

print(a_sum)