k = input().upper()

a = ['ABC', 'DEF', 'GHI', 'JKL', 'MN0', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for i in range(len(k)):
    for j in range(len(a)):
        if ((k[i] in a[j]) == True):
            cnt += (j+3)
        # if i in a[j]:
        #     cnt += a.index(i) + 3
print(cnt)
