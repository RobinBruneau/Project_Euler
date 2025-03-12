from tools import *

l_premiers = nombres_premiers_inf_k(10000)

for k in range(3,10001,2):
    if k not in l_premiers :
        ind = 0
        is_Goldbach = False
        while l_premiers[ind] <= k and (not is_Goldbach) :
            v = k-l_premiers[ind]
            r = v/2
            if int(r) == r :
                racine = np.sqrt(r)
                if int(racine) == racine :
                    is_Goldbach = True
                    print(k,l_premiers[ind],racine)
            ind += 1

        if not is_Goldbach :
            print(k)
            break