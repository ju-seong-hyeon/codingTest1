def dfs(lev, loc):
    global cnt
    if(lev == len_n):
        cnt += 1
        for i in range(0, loc):
            print(chr(arr[i] + 64) , end=" ")
        print()
    else:
        cur1 = arr_n[lev]
        cur1 = int(cur1)

        #print(chr(cur1 + 64))
        if(1<=cur1<=9):
            #print(cur1)
            arr[loc] = cur1
            dfs(lev + 1, loc + 1)

        if(lev < len_n - 1):
            cur1 = arr_n[lev]
            cur2 = arr_n[lev+1]
            cur = cur1 + cur2
            cur = int(cur)

            if(10 <= cur <= 26):
                #print(cur)
                #print(chr(cur + 64), end=" ")
                arr[loc] = cur
                dfs(lev+2, loc+1)

if __name__ == "__main__":
    n = 115213102120131
    arr_n = list(str(n))
    len_n = len(arr_n)
    arr = [0] * (len_n + 3)
    cnt = 0
    dfs(0, 0)
    print(cnt)