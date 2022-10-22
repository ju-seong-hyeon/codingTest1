a = input()
b = ""
for i in a:
    if '0' <= i <= '9':
      b += i

b = int(b)
cnt = 0
for i in range(1, b//2+1):
    if(b % i == 0):
        cnt += 1

print(b)
print(cnt + 1)