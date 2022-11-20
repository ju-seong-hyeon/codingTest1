from collections import deque
MAX = 10000
dis = [0] * (MAX+1)
ch = [False] * (MAX+1)
n, m = map(int, input().split())
ch[n] = True
dq = deque()
dq.append(n)
while(dq):
    cur = dq.popleft()
    print(cur)
    if(cur == m):
        print(dis[cur])
        break
    else:
        for i in (-1, +1, 5):
            v = cur + i
            if(1<=v<=MAX):
                if(ch[v] == False):
                    dq.append(v)
                    dis[v] = dis[cur] + 1
                    ch[v] = True
