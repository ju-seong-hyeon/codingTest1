n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cnt = 0
while(a):
    if(a[0] + a[-1] <= m):
        a.pop()
        a.pop(0)
        cnt += 1
    else:
        a.pop()
        cnt += 1

print(cnt)