def func(n):
    if(n>0):
        b = n%2
        func(n//2)
        print(b, end = "")

n = int(input())
func(n)
