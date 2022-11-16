# a, b = (input().split())
a = 5276823
b = 3

a_list = list(map(int, str(a)))
ret = []
cnt = 0
while(a_list):
    v = a_list.pop(0)
    while(len(ret)>0 and b>0 and ret[-1] < v):
        ret.pop()
        b-=1
    ret.append(v)

while(b>0):
    ret.pop()
    b-=1

for i in ret:
    print(i, end ="")