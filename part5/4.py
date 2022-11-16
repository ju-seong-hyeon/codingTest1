# n, m = map(int, input().split())
# a = list(map(int, input().split()))
n = 6
m = 0
a = [6, 6, 9, 6, 6, 6]
#
# while(a):
#     v = a.pop(0)
#     for i in a:
#         if(i > v):
#             a.append(v)
#             break
#     else:
#
a_list = []
for i, v in enumerate(a):
    a_list.append((i, v))
cnt = 0
while(a_list):
    cur = a_list.pop(0)
    for i in a_list:
        if(cur[1] < i[1]):
            a_list.append(cur)
            break
    else:
        cnt += 1
        if(cur[0] == m):
            break
    print(cur)
print(cnt)





