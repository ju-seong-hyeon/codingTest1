# 정렬 - 피보나치 수열
n = int(input())
a = [0] * (n+3)
a[1] = 0
a[2] = 1
for i in range(3, n+2):
    a[i] = a[i-1] + a[i-2]

print(a[n+1])