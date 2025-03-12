import numpy as np

num_min = 1
denum_min = 3
num_max = 3
denum_max = 7
for d in range(4,1000000+1):
    b_inf = num_min*d/denum_min
    b_sup = num_max * d / denum_max
    if np.floor(b_sup) == b_sup :
        b_sup -= 1
    for n in range(int(np.floor(b_inf)+1),int(np.floor(b_sup)+1)):
        num_min = n
        denum_min = d
        print(n,d)
