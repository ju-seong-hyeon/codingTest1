n, m = map(int, input().split())
if(n==0 and m < 45):
    n = 23
    m += 15
else:
    if(m < 45):
        n -= 1
        m += 15
    else:
        m -= 45

print(n, m)