n = int(input())
a = []
a_sum = n * 100
for i in range(n):
    n, m = map(int, input().split())
    for j in a:
        cur = j
        x = abs(cur[0] - n)
        y = abs(cur[1] - m)
        if(x < 10 and y < 10):
            a_sum -= ((10 - x) * (10 - y))
    a.append((n, m))
print(a_sum)