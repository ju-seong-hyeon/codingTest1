# 정렬 - 나이순정렬
n = int(input())
a = []
for i in range(n):
    x, y = map(str, input().split())
    x = int(x)
    a.append((x, y))
a.sort(key=lambda a:int(a[0]))
for x, y in a:
    print(x, y)