n = int(input())

cnt = 0
for i in range(n):
    v = input()
    v = list(v)
    for i in range(len(v) - 1):
        if(v[i] == v[i+1]):
            v[i] = ''
    v = ' '.join(v).split()
    if(len(v) == len(set(v))):
        cnt += 1
print(cnt)