from tools import *


n=7
l_premiers = nombres_premiers_inf_k(10**n)
print("premiers done")
bigger = 0
for e in l_premiers :
    str_prem = str(e)
    is_pandigital = True
    for nn in range(n):
        if str(nn+1) not in str_prem :
            is_pandigital = False
    if is_pandigital :
        if e > bigger :
            bigger = e
print(bigger)
