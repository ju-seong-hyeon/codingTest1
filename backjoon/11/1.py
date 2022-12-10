# 재귀 - 팩토리얼
def fac(n):
    global v
    if(n>=1):
        v *= n
        # print(v)
        fac(n-1)
    else:
        return

n = int(input())
v = 1
fac(n)
print(v)