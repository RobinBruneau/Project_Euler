
import copy
from tqdm import tqdm



def comb_entier(k,n):

    if k>n:
        return 0
    else :
        if k==1 :
            return 1
        elif k==n:
            return 1
        else :
            total = 0
            for v in range(1,k+1):
                total += comb_entier(v,n-k)
            return total

max_n = 100
total = 0
for k in range(2,101):
    v = comb_entier(k,max_n)
    print(k,v)
    total += v
print(total)

