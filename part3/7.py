n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ll = n // 2
lr = n // 2 + 1
a_sum = 0

for i in range(0, n):
    for j in range(ll, lr):
        a_sum += a[i][j]

    if(i < n // 2):
        ll -= 1
        lr += 1
    else:
        ll += 1
        lr -= 1

print(a_sum)
