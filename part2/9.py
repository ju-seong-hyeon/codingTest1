n = int(input())
a = list(map(int, input().split()))

a_sum = 0
cur = 0
for i in a:
    if(i == 1):
        cur += 1
        a_sum += cur
    else:
        cur = 0


print(a_sum)