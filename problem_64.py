import numpy as np
import copy
def canonical_sqrt(S):

    a0 = int(np.floor(np.sqrt(S)))
    if a0*a0 != S:
        m = 0
        d = 1
        a = copy.copy(a0)
        l_3 = [(a,m,d)]
        while True:

            m = int(d*a-m)
            d = int((S-m*m)/d)
            a = int(np.floor((a0+m)/d))
            if (a,m,d) in l_3 :
                return (len(l_3)-1)%2
            else :
                l_3.append((a,m,d))
    else :
        return 0



sum_odd = 0
for n in range(2,10001):
    sum_odd  += canonical_sqrt(n)
print(sum_odd)


