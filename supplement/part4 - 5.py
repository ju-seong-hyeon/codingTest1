n = 5
a = [[1, 4], [2, 3],[3, 5], [4, 6], [5, 7]]
temp = [[0, 0] for _ in range(n)]
print(temp)
for i in range(n):
    temp[i][0] = a[i][1]
    temp[i][1] = a[i][0]

print(temp)
temp.sort()
print(temp)
for i in range(n):
    a[i][0] = temp[i][1]
    a[i][1] = temp[i][0]

print(a)