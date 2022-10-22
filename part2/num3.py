n = int(input())
a = list(map(int, input().split()))

avg = sum(a)/n
avg = avg + 0.5
avg = int(avg)

val = 0
cur = 100
for i, v in enumerate(a):
    val = abs(v - avg)

    if(val < cur):
        cur = val
        cur_i = i+1
        cur_v = v
    elif(val == cur):
        if(v > cur_v):
            cur_v = v
            cur_i = i+1

print(avg, cur_i)



