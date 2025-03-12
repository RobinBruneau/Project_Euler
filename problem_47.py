from tools import *

n=134044

l_premiers = nombres_premiers_inf_k(n+1)

d1 = div_premier(1,l_premiers)
d2 = div_premier(2, l_premiers)
d3 = div_premier(3, l_premiers)
for k in range(4,n+1):
    d4 = div_premier(k+3, l_premiers)
    if len(d1) == 4 & len(d2) == 4 and len(d3) == 4 & len(d4) == 4 :
        print("4")
        print(k,k+1,k+2,k+3)
        print(d1,d2,d3,d4)
    d1 = d2
    d2 = d3
    d3 = d4
    a=0