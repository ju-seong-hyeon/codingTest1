n = int(input())
a = []
len_max = 0
len_min = 50
for i in range(n):
    k = input()
    a_len = len(k)
    # if(len_max < a_len):
    #     len_max = a_len
    # if(len_min > a_len):
    #     len_min = a_len
    a.append((a_len, k))
# b = [[] * n for _ in range(n)]
a = list(set(a))
a = sorted(a)
for i, v in a:
    print(v)

# for x, y in a:
#     b.append(y)
# print(b)
# c = []
# for i in range(len(b)):
#     b[i] = sorted(b[i])
# print(b)

# print(len_min, len_max)
# for i in a:
#     a_len = len(i)
#
#     for l in range(len_min, len_max+1):
#         # print(len)
#         if(a_len == l):
#             b.append(i)
#     if(b):
#         print(b)
#         # b.sort()
#         # # print(b)
#         # for j in b:
#         #     c.append(j)
#         b.clear()
#
# # for i in c:
# #     print(i)


