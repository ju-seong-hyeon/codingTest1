n = 5
a = [[25,3,4],[4,4,6],[9,2,3],[16,2,5],[1,5,2]]
# a.insert(0, 0)
# print(a)
a.sort(reverse= True)
# 벽돌 최대 100개,
# 밑면 넓이, 벽돌의 높이, 무게
# 가장 높이 쌓을 수 있는 납의 높이
# ---조건---
# 밑면이 좁은 벽들 위에 밑면이 넓은 벽들을 놓을 수 없음
# 무게가 무거운 벽을들 무게가 가벼운 벽들 위 에 놓을 수 없다.
res = [0] * n
res[0] = a[0][1]
for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if(a[j][2] > a[i][2] and res[j] > max_h):
            max_h = res[j]
    res[i] = max_h + a[i][1]

print(res)