arr = []
for i in range(1, 20+1):
    arr.append(i)


for _ in range(10):
    a, b = map(int, input().split())
    brr = []
    brr = arr[a-1 : b]
    brr = brr[::-1]
    arr[a-1: b] = brr

print(arr)
