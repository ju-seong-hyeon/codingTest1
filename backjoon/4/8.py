n = int(input())
# a = 'OOXXOXXOOO'
# a = list(a)

for _ in range(n):
    a = input()
    a = list(a)
    cnt = 0
    a_sum = 0
    for i in a:
        if i == 'O':
            cnt += 1
            a_sum += cnt
        else:
            cnt = 0
    print(a_sum)