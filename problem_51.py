from tools import *
import numpy as np
import copy

n=1000000
l_premiers = nombres_premiers_inf_k(n)
l_premiers = np.array(l_premiers)
l_premiers = l_premiers[np.where(l_premiers>99999)]
l_premiers = l_premiers.tolist()
l_premier_dec = []
for premier in l_premiers :
    l_premier_dec.append(np.array(list(str(premier))).astype(int))
l_premier_dec = np.array(l_premier_dec)

cb_k_n = []
inv_k_n = []

def rec_k_n(k,n,lv=[]):

    if len(lv) == 0 :
        for ll in range(n):
            lv.append([ll])

    if k<=1:
        return lv

    new_lv = []
    for indv in range(len(lv)) :
        last = lv[indv][-1]
        for kk in range(last+1,n):
            v = copy.deepcopy(lv[indv])
            v.append(kk)
            new_lv.append(v)
    return rec_k_n(k-1,n,new_lv)



a=0
max_same = 0
for ind in range(2,6):
    l_exact = rec_k_n(ind, 6)
    for exact in l_exact :
        for ind_p in range(l_premier_dec.shape[0]) :
            premier = l_premier_dec[ind_p]
            premier_in = premier[exact]
            if len(np.unique(premier_in)) == 1 :
                out = [0,1,2,3,4,5]
                for e in exact :
                    out.remove(e)

                l_premier_dec_spe = l_premier_dec[ind_p:,:]

                premier_out = premier[out]
                l_prem_dec_out = l_premier_dec[:,out]
                l_prem_dec_exact = l_premier_dec[:, exact]
                l_prem_dec_out_diff = abs(l_premier_dec[:,out] - premier_out)
                diff_sum = np.sum(l_prem_dec_out_diff,axis=1)
                ind_0 = np.where(diff_sum==0)
                diff_sum_0 = l_prem_dec_out[ind_0]
                diff_sum_exact =  l_prem_dec_exact[ind_0]
                diff_sum_all = l_premier_dec[ind_0]
                a=0
                nb_same = 0
                ind_same = []
                it = 0
                for e in diff_sum_exact :
                    if len(np.unique(e)) == 1:
                        nb_same += 1
                        ind_same.append(it)
                    it += 1
                if nb_same > max_same :
                    max_same = nb_same
                    print(nb_same)
                    print(diff_sum_all[ind_same])
                    print("")