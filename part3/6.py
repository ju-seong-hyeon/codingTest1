n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a_max = 0
a_max1 = 0
a_max2 = 0

for i in range(0, n):
    a_max1 += a[i][i]
    a_max2 += a[n-1-i][i]
    a_max3 = 0
    a_max4 = 0
    for j in range(0, n):
        a_max3 += a[i][j]
        a_max4 += a[j][i]
    a_max = max(a_max, a_max3)
    a_max = max(a_max, a_max4)
    print(a_max3, a_max4)

print(a_max1, a_max2)
a_max = max(a_max, a_max1, a_max2)
print(a_max)
