from tools import *
import numpy as np

l_premiers = np.array(nombres_premiers_inf_k(10000))
l_premiers = l_premiers[np.where(l_premiers>999)]

def is_permutation(i,j,k):
    li = list(str(i))
    lj = list(str(j))
    lk = list(str(k))
    for e in li :
        if e not in lj :
            return False
        else :
            lj.remove(e)
        if e not in lk :
            return False
        else :
            lk.remove(e)
    return len(lj) == 0 and len(lk)==0



for k in range(len(l_premiers)):
    for j in range(k+1,len(l_premiers)):
        i = 2*l_premiers[j]-l_premiers[k]
        if in_list(l_premiers,i):
            if is_permutation(l_premiers[k],l_premiers[j],i):
                print(l_premiers[k],l_premiers[j],i)
