n = int(input())
a = list(map(int, input().split()))


str = str()
cnt = 0
cur = 0

if(a[0] <= a[-1]):
    cnt += 1
    cur = a.pop(0)
    str += "L"
else:
    cnt += 1
    cur = a.pop()
    str += "R"

while(a):
    if(cur < a[0] and cur < a[-1]):
        if (a[0] <= a[-1]):
            cnt += 1
            cur = a.pop(0)
            str += "L"
        else:
            cnt += 1
            cur = a.pop()
            str += "R"
    elif(cur < a[0]):
        cnt += 1
        cur = a.pop(0)
        str += "L"
    elif(cur < a[-1]):
        cnt += 1
        cur = a.pop()
        str += "R"
    else:
        break
print(cnt)
print(str)
