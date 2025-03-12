import numpy as np

l_premiers = [2,3,5,7]

n = 11
while len(l_premiers) != 10001 :

    racine = int(np.sqrt(n))

    lp = np.array(l_premiers)
    lp = lp[np.where(lp<=racine)]
    restes = n % lp
    zero = len(np.where(restes == 0)[0])

    if zero == 0 :
        l_premiers.append(n)

    n+=2

print(l_premiers[-1])
