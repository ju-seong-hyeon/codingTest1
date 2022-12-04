a = [0] * 27
s = input()
s = s.upper()

# print(ord('A'))

for j in s:
    a[ord(j) - 64] += 1


a_max = max(a)
if(a.count(a_max) >= 2):
    print("?")
else:
    for i in range(1, 27):
        if(a_max == a[i]):
            print(chr(i+ 64))

