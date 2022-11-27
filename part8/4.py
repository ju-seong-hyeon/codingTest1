n = 10
a = [4,1,2,3,9,7,5,6,10,8]
a.insert(0, 0)
res = [0] * (n+1)
res[1] = 1

for i in range(2, n+1):
    a_max = 0
    for j in range(i-1, 0, -1):
        if(a[i] > a[j] and res[j] > a_max):
            a_max = res[j]
    res[i] = a_max + 1

print(res)
