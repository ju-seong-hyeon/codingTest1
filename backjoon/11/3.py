#브루트포스 - 블랙잭
def dfs(lev, tot, ret):
    global a_sum
    if(tot > m):
        return
    if lev == k:
        a_sum = max(tot, a_sum)
    else:
        for i in range(ret, n):
            dfs(lev+1, tot + a[i], i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    k = 3
    a = list(map(int,input().split()))
    a_sum = 0
    dfs(0, 0, 0)
    b = [0] * (k+1)
    print(a_sum)