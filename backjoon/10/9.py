n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key = lambda x : (x[1], x[0]))
for x, y in a:
    print(x, y)