n = 5
a = [[25,3,4],[4,4,6],[9,2,3],[16,2,5],[1,5,2]]
res = [0] * n
a.sort(reverse=True)
# 밑면넓이, 높이, 무게

for i in range(n):
    a_max = 0
    for j in range(i-1, -1, -1):
        if(a[j][2] > a[i][2] and a_max < res[j]):
            a_max = res[j]
    res[i] = a_max + a[i][1]
print(max(res))