import bisect

def p_suite(n):
    l_penta = []
    for v in range(1,n+1):
        l_penta.append(int(v*(3*v-1)/2))

    return l_penta

def t_suite(n):
    l_tri = []
    for v in range(1,n+1):
        l_tri.append(int(v*(v+1)/2))

    return l_tri

def h_suite(n):
    l_hex = []
    for v in range(1,n+1):
        l_hex.append(int(v*(2*v-1)))

    return l_hex

def in_list(l, e):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(l, e)
    if i:
        return l[i-1] == e
    else :
        return False

n=100000
lp = p_suite(n)
lt = t_suite(n)
lh = h_suite(n)

for e in lp :
    if in_list(lt,e) and in_list(lh,e):
        print(e)