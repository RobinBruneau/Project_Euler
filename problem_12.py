import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np


def div_premier(n,l_premiers):

    l=[]
    k=0
    while n != 1 :
        reste = n%l_premiers[k]
        nb = 0
        while reste == 0 :
            n /= l_premiers[k]
            nb+=1
            reste = n%l_premiers[k]
        if nb != 0:
            l.append(nb)
        k+=1

    prod = 1
    for e in l :
        prod *= (e+1)

    return prod



l_premiers = [2,3,5,7]

n = 11
continuer= True
sum = 0
while continuer :

    racine = int(np.sqrt(n))

    is_premier = True
    ind = 0
    while l_premiers[ind] <= racine and is_premier:
        reste = n % l_premiers[ind]
        if reste ==  0 :
            is_premier = False
        ind+=1

    if is_premier :
        l_premiers.append(n)
        sum += n

    n+=2
    if n >= 200000 :
        continuer = False

n=22
continuer = True
val = []
while continuer :
    triangle = int(n*(n+1)/2)

    nb_div = div_premier(triangle,l_premiers)
    val.append(nb_div)
    if nb_div > 500 :
        print(n,triangle)
        continuer = False

    if n==3024:
        print(nb_div)
    n+=1

plt.plot(val)
plt.show()


