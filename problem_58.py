import numpy as np
from tools import *



l_premiers = nombres_premiers_inf_k(30001)
inf_10_pc = False
nb_premiers_diag = 0
multi = 0
stop = 1
n = 3
while not inf_10_pc :
    multi += 2
    nb_pts = multi*2+1
    l_check = []
    for jj in range(4):
        n = stop+(jj+1)*multi
        racine = int(np.sqrt(n))
        is_premier = True
        ind = 0
        while l_premiers[ind] <= racine and is_premier:
            reste = n % l_premiers[ind]
            if reste == 0:
                is_premier = False
            ind += 1

        if is_premier:
            nb_premiers_diag += 1
    #print(l_check)
    stop += 4*multi

    if nb_premiers_diag*10 < nb_pts :
        inf_10_pc = True
        print(multi+1,nb_premiers_diag/nb_pts)
    else :
        print(multi+1,nb_premiers_diag/nb_pts)

