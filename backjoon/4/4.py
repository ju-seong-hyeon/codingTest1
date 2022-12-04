a = []
for _ in range(9):
    m = int(input())
    a.append(m)
a_max = 0
a_idx = 0
for i, v in enumerate(a):
    if(a_max < v):
        a_max = v
        a_idx = i
print(a_max)
print(a_idx + 1)
