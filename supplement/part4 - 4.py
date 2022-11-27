def func(mid):
    cnt = 1
    cur = a[0]
    for i in a:
        if(i - cur >= mid):
            cnt += 1
            cur = i
    return cnt

if __name__ == "__main__":
    # n = 5
    # c = 3
    # a = [1,2,8,4,9]
    n = 64
    c = 19
    a = [8,
11,
18,
37,
57,
65,
83,
101,
112,
115,
129,
130,
146,
149,
153,
159,
166,
167,
172,
191,
201,
205,
227,
228,
234,
272,
273,
282,
295,
319,
340,
394,
398,
399,
436,
446,
453,
481,
499,
503,
611,
655,
680,
692,
718,
725,
726,
735,
739,
778,
811,
839,
841,
852,
867,
882,
907,
915,
923,
943,
956,
967,
970,
989
]
    a.sort()

    ll = a[0]
    lr = a[-1]
    a_max = 0
    while(ll<=lr):
        mid = (ll + lr) // 2

        cnt = func(mid)
        if(cnt == c):
            ll = mid + 1
            a_max = max(mid, a_max)
        elif(cnt < c):
            lr = mid - 1
        else:
            ll = mid + 1
    print(a_max)

