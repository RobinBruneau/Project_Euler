import numpy as np
from tools import *
from tqdm import tqdm

l_premiers = nombres_premiers_inf_k(1000000)
max_tot = 0
ind_max_tot = 0
for k in tqdm(range(2,1000001)):

    if k%2 == 0 and k%3==0 :
        div_p = div_premier(k,l_premiers)

        phi = 1
        for prem in div_p :
            phi *= (prem[0]-1)*prem[0]**(prem[1]-1)

        totient = k/phi

        if totient > max_tot :
            max_tot = totient
            ind_max_tot = k

print(ind_max_tot)