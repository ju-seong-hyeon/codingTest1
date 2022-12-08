n,m,k = map(int, input().split())


if(n == 0):
    if(k == m):
        print(-1)
    elif(k>m):
        print(1)
    else:
        print(-1)

else:

    if(k == m):
        print(-1)
    elif(k > m):
        anw = n / (k - m)
        anw = anw + 1
        anw = int(anw)
        print(anw)
    else:
        # (k < m)
        print(-1)