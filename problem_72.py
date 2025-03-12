import numpy as np
from tools import *
from tqdm import tqdm

'''
d= 12

l_premiers = nombres_premiers_inf_k(d)

total_add = 0
l_remove = []
for k in range(0,d+1):
    l_remove.append([0,-1])

for k in tqdm(range(2,d+1)):
    total_add += k-1
    divp = div_premier(k,l_premiers)
    steps = [int(k[0]) for k in divp]
    for step in steps :
        for it in range(k+step,d+1,step):
            if l_remove[it][1] != k :
                l_remove[it][0] += 1
                l_remove[it][1] = k

total_remove = np.sum([k[0] for k in l_remove])
total = total_add - total_remove
a=0
'''

def denombrement_doublons_under_k(divp,k):
    max_pow = []
    for div in divp :
        max_float = np.log(k+1)/np.log(div)
        if max_float == np.floor(max_float):
            max_pow.append(int(np.floor(max_float))-1)
        else :
            max_pow.append(int(np.floor(max_float)))

    a=0

d= 1000000

l_premiers = nombres_premiers_inf_k(d)

total_add = 0
l_remove = []
for k in range(0,d+1):
    l_remove.append([0,-1])

for k in tqdm(range(2,d+1)):
    total_add += k-1
    divp = div_premier(k,l_premiers)
    steps = [int(k[0]) for k in divp]
    # N + divp < d
    #n_remove = denombrement_doublons_under_k(steps,d-k)
    a=0