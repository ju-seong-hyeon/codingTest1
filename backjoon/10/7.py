n = int(input())
n = list(map(int, str(n)))

n.sort(reverse = True)
for i in n:
    print(i, end = '')