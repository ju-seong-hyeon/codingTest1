a = '()(((()())(())()))(())'
a_list = list(a)
print(a_list)
b = []
ret = 0
for i in range(len(a_list)):
    if(a_list[i] == '('):
        b.append(a_list[i])
    else:
        b.pop()
        if(a_list[i-1] == '('):
            ret += len(b)
        else:
            ret+=1
print(ret)

