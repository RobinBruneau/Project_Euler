import bisect


def pentagon_suite(n):
    l_penta = []
    for v in range(1,n+1):
        l_penta.append(int(v*(3*v-1)/2))

    return l_penta


def in_list(l, e):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(l, e)
    if i:
        return l[i-1] == e
    else :
        return False

n=10000
lp = pentagon_suite(10*n)

for e1 in range(n):
    for e2 in range(e1+1,n):
        if in_list(lp,lp[e2]+lp[e1]) :
            #print(lp[e1],lp[e2],lp[e1]+lp[e2])
            if in_list(lp,lp[e2] - lp[e1]):
                print(lp[e1], lp[e2], lp[e1] + lp[e2],lp[e2] - lp[e1])
