arr = [[0] * 101 for i in range(101)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1
a_sum = 0
for i in arr:
    a_sum += sum(i)
print(a_sum)