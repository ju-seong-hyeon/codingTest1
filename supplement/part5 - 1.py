# n = 5276823
# m = 3
n = 9977252641
m = 5
n = list(str(n))
print(n)
arr = []

for i in n:
    while(arr and m > 0 and arr[-1] < i):
        m-=1
        arr.pop()
    arr.append(i)
if(m>0):
    for i in range(m):
        arr.pop()

print(arr)
for i in arr:
    print(i, end="")
