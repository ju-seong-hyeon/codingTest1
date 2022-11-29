n = 10
a = [4, 1, 2, 3, 9, 7, 5, 6, 10, 8]
a.insert(0, 0)
arr = [0] * (n+1)
arr[1] = 1
for i in range(2, n+1):
    arr_max = 0
    for j in range(i, 0, -1):
        if(a[i] > a[j] and arr_max < arr[j]):
            arr_max = arr[j]
    arr[i] = arr_max + 1
print(arr)
print(max(arr))