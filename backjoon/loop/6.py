n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a += b
    print("Case #%d: %d" %((i+1), a))