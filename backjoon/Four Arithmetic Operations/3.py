# a = 472
# b = 385
a = int(input())
b = int(input())
#a = list(map(int, str(a)))
b = list(map(int, str(b)))
c = []
n = len(b)

for j in range(n-1, -1, -1):
    a_sum = 0
    a_sum += (a * b[j])
    fac = 10 ** abs(j + 1 - n)
    print(a_sum)
    if(fac == 0):
        c.append(a_sum)
    else:
        c.append(a_sum * fac)



    #print()
#print(c)
print(sum(c))
# 2 -> 0
# 1 -> 1
# 0 -> 2