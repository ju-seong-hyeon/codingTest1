n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
a = sorted(a)

for x,y in a:
    print(x, y)
