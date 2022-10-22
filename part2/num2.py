num = int(input())
for i in range(num):
    N, s,e, k = map(int,input().split())
    a = list(map(int, input().split()))

    b = a[s-1: e]
    b.sort()
    print("#%d %d" %(i+1, b[k-1]))