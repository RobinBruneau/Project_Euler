
import copy
from tqdm import tqdm
from tools import *


def comb_entier_prem(n,lp):
    slp = [p for p in lp if p<=n]
    total = 0
    for p in slp :
        total += comb_prem_max_k(p,n,slp)
    return total
def comb_prem_max_k(k,n,lp):

    if k>n:
        return 0
    else :
        if k==n:
            return 1
        else :
            total = 0
            ind_k = lp.index(k)
            for v in range(ind_k+1):
                total += comb_prem_max_k(lp[v],n-k,lp)
            return total

max_n = 100
lp = nombres_premiers_inf_k(100)
for n in range(2,max_n+1):
    vv = comb_entier_prem(n,lp)
    print(n,vv)
    if vv > 5000:
        break
