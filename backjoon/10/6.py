n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
avg = sum(a) / len(a)
print('{:.0f}'.format(avg))
print(a[n//2])


a_min = min(a)
v = max(a) - a_min
cnt = a.count(a_min)
if(cnt > 1):
    for i in range(cnt):
        a.remove(a_min)
    print(min(a))
else:
    print(a_min)

print(v)