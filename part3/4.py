n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a = a + b
a.sort()
print(a)