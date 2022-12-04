T = int(input())
for i in range(T):
    a = list(input())
    for i in range(2, len(a)):
        v = a[i]
        val = v * int(a[0])
        print(val, end = "")
    print()