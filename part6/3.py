def dfs(v, val):
    if(v == n):
        return
    if(val > a_sum//2 + 1):
        return
    elif(val == a_sum-val):
        print("YES")
        exit()
    else:
        dfs(v+1, val+a[v])
        dfs(v+1, val)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    cur_v = 0
    dfs(0, 0)
    print("NO")
