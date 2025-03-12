import numpy as np
from tools import *
import time


def comb_prem_under_k(l_prem,k,ind_loc=0,prod=1):

    if l_prem[ind_loc] <= np.sqrt(k) :

        # recurcive with older one
        l_keep = []
        ind_pow = 1
        total_prod = prod*(l_prem[ind_loc]**ind_pow)
        while total_prod < k:
            l_sub_keep = comb_prem_under_k(l_prem,k,ind_loc+1,total_prod)
            ind_pow += 1
            l_keep.append(total_prod)
            l_keep = l_keep + l_sub_keep
            total_prod = prod * (l_prem[ind_loc] ** ind_pow)


    return l_keep


t0 = time.time()
l_prem = nombres_premiers_inf_k(31623)
k = 10**9
l_keep = comb_prem_under_k(l_prem,k)
l_keep = np.array(tri_fusion(l_keep))


continuer = True
keep_ind = 0
l_keep_pseudo_f = []
while continuer :
    keep = l_keep[keep_ind]
    test_prime = keep+3
    while not is_prime(test_prime):
        test_prime += 2

    while keep_ind < len(l_keep) and test_prime > 2 + l_keep[keep_ind] :
        l_keep_pseudo_f.append(test_prime)
        keep_ind += 1

    if keep_ind >= len(l_keep):
        continuer = False

l_keep_pseudo_f = np.array(l_keep_pseudo_f)
diff = l_keep_pseudo_f-l_keep
diff_dist = np.array(list(set(diff)))
print(np.sum(diff_dist))
print(time.time()-t0)