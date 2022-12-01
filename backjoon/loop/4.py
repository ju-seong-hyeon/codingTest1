n = int(input())
p = int(input())
a = []
for i in range(p):
    r,t = map(int, input().split())
    a.append((r, t))
a_sum = 0
for i in range(p):
    a_sum += (a[i][0] * a[i][1])

if(n == a_sum):
    print("Yes")
else:
    print("No")