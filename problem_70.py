from tools import *

def is_perm(a,b):
    return sorted(str(a)) == sorted(str(b))

n = 100000000
max_n = math.ceil(math.sqrt(n))+1


lp = nombres_premiers_inf_k(max_n)
min_ff = 10
for k in range(len(lp)):
    for j in range(k,len(lp)):
        p1 = lp[k]
        p2 = lp[j]
        prod_p = p1 * p2
        if prod_p < 10000000:
            phi_prod_n = (p1 - 1) * (p2 - 1)
            ff = prod_p / phi_prod_n
            if is_perm(prod_p, phi_prod_n):
                if ff < min_ff :
                    min_ff = ff
                    print(prod_p,phi_prod_n, ff)