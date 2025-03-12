from tools import *

n=1000000
l_premiers = nombres_premiers_inf_k(n)

max_it = 0
for k in range(len(l_premiers)) :
    sum = 0
    it = 0
    j= k+1
    while sum < n and j<len(l_premiers) :
        sum += l_premiers[j]
        it += 1
        if  sum != l_premiers[j] and in_list(l_premiers,sum) :
            if it > max_it :
                print(it,sum)
                max_it = it
        j+=1