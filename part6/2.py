def dfs(v):
    global cnt
    if(v == n+1):
        for i in range(1, n+1):
            if a[i] == 1:
                print(i, end =" ")
        print()
        cnt += 1
    else:
        a[v] = 1
        dfs(v+1)
        a[v] = 0
        dfs(v+1)

if __name__ == "__main__":
    cnt = 0
    n = int(input())
    a = [0] * (n+1)
    dfs(1)
    print(cnt)

