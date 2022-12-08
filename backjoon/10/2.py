n = 5
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
print(int(sum(arr)/ n))
print(arr[n//2])