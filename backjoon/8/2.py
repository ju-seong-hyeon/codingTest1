a = [list(map(int, input().split())) for _ in range(9)]

a_max = 0
a_x = 0
a_y = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if(a_max < a[i][j]):
            a_max = a[i][j]
            a_x = i
            a_y = j

print(a_max)
print(a_x+1, a_y+1)
