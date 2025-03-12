import numpy as np

def find_rec_div_n(n):

    l_visited = []
    l_ind = []
    ind=0
    left = 1
    while left < n :
        left *= 10

    while True :
        ind += 1
        reste = left%n

        if reste == 0 :
            return -1
        else :
            left = reste*10
        if reste not in l_visited :
            l_visited.append(reste)
            l_ind.append(ind)
        else :
            ind_b = l_visited.index(reste)
            return ind-l_ind[ind_b]

max_rec = -1
ind_rec = None
for k in range(2,1001):

    val = find_rec_div_n(k)
    if val > max_rec :
        max_rec = val
        ind_rec = k

print(max_rec,ind_rec)