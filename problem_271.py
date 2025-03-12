import numpy as np
import math
from tools import in_list
import bisect
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
np.random.seed(3)

def jeu(p):

    L = []
    l_c = np.arange(0, 1000)
    win = False
    it = 1
    while not win :
        nb = np.random.choice(l_c,p=p/np.sum(p))
        if in_list(L,1000-nb) :
            return it
        else :
            it += 1
            p[nb-1] -= 1
            bisect.insort(L,nb)

p = []
for k in range(1000):
    p.append(26**3)

nb_jeu = 100000
nb_it = 0
l_moy = []
l_it = []
for k in tqdm(range(nb_jeu)):
    result = jeu(p)
    l_it.append(result)
    nb_it += result
    l_moy.append(nb_it/(k+1))

print(l_moy[-1])
plt.figure()
plt.plot(abs(np.array(l_moy[:-1])-l_moy[-1]))
plt.gca().set_yscale('log')

plt.figure()
nb = len(set(l_it))
plt.hist(l_it,bins=nb)
plt.show()
