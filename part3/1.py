n = int(input())
for i in range(n):
    a = input()
    a = a.upper()
    for j in range(len(a)//2):
        if(a[j] != a[len(a)-j-1]):
            print("#%d No" %(i+1))
            break
    else:
        print("#%d Yes" %(i+1))