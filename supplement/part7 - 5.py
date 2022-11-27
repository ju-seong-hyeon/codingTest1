def dfs(lev, val):
    global cnt
    if(lev == n_n):
        for i in range(val):
            a[i] = int(a[i])
            print(chr(a[i] + 64), end = "")
        print()
    else:
        a_cur = n[lev]
        a[val] = a_cur
        dfs(lev+1,val+1)

        if(lev != n_n-1):
            a_cur = (n[lev] + n[lev])
            if('10'<= a_cur<= '26'):
                a[val] = a_cur
                dfs(lev+2,val+1)


if __name__ == "__main__":
    n = 25114
    n = list(str(n))
    n_n = len(n)
    #print(chr(2 + 64))
    a = [0] * (n_n+3)
    cnt = 0
    dfs(0, 0)
    print(cnt)