n = 5
a = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]
a.sort(reverse = True)
print(a)
a_max = 0
cnt = 0

for i in a:
    if(i[1] > a_max):
        cnt += 1
        a_max = i[1]
print(cnt)