# curi = input()
# m = int(input())
# for i in range(m):
#     cur = input()
from collections import deque

# curi = 'CBA'
# m = int(input())
# cur = ['CBDAGE', 'FGCDAB', 'CTSBDEA']
#
# for i in cur:
#     put_curi = list(curi)
#     while (put_curi):
#         j = put_curi.pop(0)
#         for ii in i:
#
#
#         if(len(put_curi) == 0):
#             print("YES")
#             break
#     else:
#         print("NO")

need = 'CBA'
n = 3
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if(x!=dq.popleft()):
                print("#%d NO" %(i+1))
                break
    else:
        if(len(dq) == 0):
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

