
import copy
from tqdm import tqdm
import numpy as np
from tools import *

def comb_entier(n,tab_k_n):
    total_n = [0]
    for k in range(1, n+1):
        v = comb_entier_k(k, n,tab_k_n)
        tab_k_n[k][n]=v
        total_n  = add(total_n,v)
    return total_n,tab_k_n
def comb_entier_k(k,n,tab_k_n):

    if k>n:
        return [0]
    else :
        if k==1 :
            return [1]
        elif k==n:
            return [1]
        else :
            if len(tab_k_n[k][n]) != 0:
                return tab_k_n[k][n]
            else :
                total = [0]
                for v in range(1,k+1):
                    val = comb_entier_k(v,n-k,tab_k_n)
                    total  = add(total,val)
                    tab_k_n[v][n-k] = val
                return total

def check_div_million(l):
    if len(l)<7 :
        return False
    else :
        return sum(l[:6])==0



max_n = 1000
tab_k_n = []
for i in range(max_n+1):
    sub_t = []
    for j in range(max_n+1):
        sub_t.append([])
    tab_k_n.append(sub_t)
for n in range(2,max_n+1):
    vv,tab_k_n = comb_entier(n,tab_k_n)
    print(n,vv)
    if check_div_million(vv):
        break
a=0