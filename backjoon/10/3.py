n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse= True)
# print(a)
print(a[m-1])