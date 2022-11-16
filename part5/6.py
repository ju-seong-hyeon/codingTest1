n = int(input())
a = {}
for _ in range(n):
    v = input()
    a[v] = 1

for _ in range(n-1):
    v = input()
    a[v] = 0

for key, value in a.items():
    if(value == 1):
        print(key)