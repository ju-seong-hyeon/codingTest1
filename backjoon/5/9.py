# k = input()
k = 'dz=ak'
k = list(k)
a = {'c=' : 'č', 'c-': 'ć', 'dz=': 'dž', 'd-': 'đ', 'lj': 'lj', 'nj': 'nj', 's=': 'š', 'z=': 'ž'}
cnt = 0
v = []
for i in range(0, len(k) - 1):
    cur = k[i] + k[i+1]
    # print(cur)
    if(cur in a.keys()):
        cnt += 1
        # print(a[cur])
        if(len(a[cur]) == 1):
            k[i] = a[cur]
            # print(a[cur])
        k[i] = a[cur]
        k[i+1] = ""
        # print(cur)

k = ' '.join(k).split()
print(k)
print(len(k))
# print(cnt)