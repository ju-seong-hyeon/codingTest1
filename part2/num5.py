n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    x_sum = 0
    x = str(x)
    for i in x:
        v = int(i)
        x_sum += v

    return x_sum
cnt = 0
for i in a:
    v = digit_sum(i)
    if(v>cnt):
        v_val = i
        cnt = v

print(v_val)