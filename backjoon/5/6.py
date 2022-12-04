a = input()
a = list(a.split(" "))
b = []
for i in range(len(a)):
    if(a[i] == ''):
        b.append(i)

for i in b:
    del(a[i])
print(len(a))

a = input().sp