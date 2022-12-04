n = 30
a = [0] * (n + 1)

for i in range(n- 2):
    m = int(input())
    a[m] = 1

for i in range(1, n+1):
    if(a[i] == 0):
        print(i)
