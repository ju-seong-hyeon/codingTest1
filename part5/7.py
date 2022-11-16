a = input()
b = input()
dic1 = {}
dic2 = {}
for i in a:
    if i in dic1.keys():
        dic1[i] +=1
    else:
        dic1[i] = 1
for i in b:
    if i in dic2.keys():
        dic2[i] +=1
    else:
        dic2[i] = 1

for k, v in dic1.items():
    if(k in dic2.keys()):
        if(v != dic2[k]):
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")