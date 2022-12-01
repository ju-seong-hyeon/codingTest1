n, m = map(int, input().split())
k = int(input())
m += k
time = m // 60
min = m % 60

n += time
if(n >= 24):
    n -= 24
print(n, min)
