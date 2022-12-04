a = set()
n = 10

for i in range(n):
    k = int(input())
    a.add(k%42)

print(len(a))