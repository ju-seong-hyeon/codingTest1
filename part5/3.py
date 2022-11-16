n = 8
m = 3
a = []

for i in range(1, n+1):
    a.append(i)

while(a):
    for i in range(m):
        v = a.pop(0)
        if(i==m-1):
            break
        a.append(v)
    if(len(a)==1):
        print(a[0])

