def reverse(x):
    x = str(x)
    x = x[::-1]
    x = int(x)
    return x

def isPrime(x):
    for i in range(2, x//2+1):
        if(x%i == 0):
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

for i in a:
    v = reverse(i)
    if(isPrime(v)):
        print(v, end = " ")