a = [-1] * (26 + 1)
s = input()
n = len(s)

# for i in range(1, 27):
#     # val = ord(s[i])
#     # print(val - 96)
#     # a[val - 96] = val - 96
#
#     for j in range(n):
#         k = (ord(s[j]) - 96)
#         if(i == k):
#             a[k] = i



#
# for i in range(1, 27):
#     a[i] = i
#     print(a[i], end = " ")

for i in range(n):
    val = ord(s[i]) - 96
    if(a[val] == -1 ):
        a[val] = i
for i in range(1, 27):
    print(a[i], end = ' ')