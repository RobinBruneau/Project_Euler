import numpy as np
from tools import *
from tqdm import tqdm

def co_prime(da,db):
    for a in da :
        if a in db :
            return False
    return True

lp = nombres_premiers_inf_k(12000)


num_min = 1
denum_min = 3
num_max = 1
denum_max = 2
in_between = 0
for d in tqdm(range(4,12000+1)):
    dd = prime_decomposition(lp,d)
    dd = [k for k in dd]
    b_inf = num_min*d/denum_min
    b_sup = num_max * d / denum_max
    if np.floor(b_sup) == b_sup :
        b_sup -= 1
    for n in range(int(np.floor(b_inf)+1),int(np.floor(b_sup)+1)):
        dn = prime_decomposition(lp,n)
        dn = [k for k in dn]
        if co_prime(dd,dn):
            in_between += 1
print(in_between)