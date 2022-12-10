#정렬 - 좌표 압축
n = int(input())
a = list(map(int, input().split()))
arr2 = sorted(list(set(a)))
print(arr2)
for i in a:
    print(arr2.index(i), end = " ")

# a = map(int, input().split())
# a.sort()
# b = []
# cnt = 0
# for i in range(1, len(a)+1):
#     if(a)