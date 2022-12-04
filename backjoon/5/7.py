n, m = input().split()
n = n[::-1]
m = m[::-1]
n = int(n)
m = int(m)
if(n > m):
    print(n)
else:
    print(m)