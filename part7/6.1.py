def dfs(v, p):
    global a_cnt
    if(v == n_len):
        a_cnt += 1
        print(ex_a)
        for i in range(p):
            print(chr(ex_a[i] + 64), end ="")
        print()
    else:
        cur = n[v]
        cur_v = int(cur)
        ex_a[p] = cur_v
        dfs(v+1, p+1)
        if(v < n_len-1):
            cur = n[v] + n[v+1]
            cur_v = int(cur)
            if(10 <= cur_v <= 26):
                ex_a[p] = cur_v
                dfs(v+2, p+1)

if __name__ =="__main__":
    n = 25114
    n = str(n)
    n_len = len(n)
    a_cnt = 0
    ex_a = [0] * (n_len+3)
    dfs(0, 0)
    print(a_cnt)

