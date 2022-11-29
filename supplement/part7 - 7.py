from collections import deque
MAX = 10000
n, m = map(int, input().split())
dq = deque()
map = [0] * (MAX + 1)
ch = [0] * (MAX + 1)
ch[n] = 1
dq.append(n)
while(dq):
    cur = dq.popleft()
    if(cur == m):
        print(map[cur])
        break
    else:
        for i in (-1, 1, 5):

            val = cur + i
            if(0<=val<=10000):
                if(ch[val] == 0):
                    map[val] = map[cur] + 1
                    dq.append(val)
                    ch[val] = 1
