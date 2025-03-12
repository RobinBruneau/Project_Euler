import numpy as np
from tqdm import tqdm

x = np.array([3,4,5]).reshape(3,1)


def all_reduc_tri(x,lmax):
    R1 = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
    R2 = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
    R3 = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

    x1 = R1 @ x
    x2 = R2 @ x
    x3 = R3 @ x

    if np.sum(x1)<lmax :
        x1_follow = [x1] + all_reduc_tri(x1,lmax)
    else :
        x1_follow = []

    if np.sum(x2)<lmax :
        x2_follow = [x2] + all_reduc_tri(x2,lmax)
    else :
        x2_follow = []

    if np.sum(x3)<lmax :
        x3_follow = [x3] + all_reduc_tri(x3,lmax)
    else :
        x3_follow = []

    return x1_follow+x2_follow+x3_follow

lmax = 1500000
results = all_reduc_tri(x,lmax=lmax)
l_sol = [12] + [int(np.sum(k)) for k in results]
a=0

compte = {}
for ls in tqdm(l_sol) :
    mult = 1
    while ls*mult < lmax :
        compte[ls*mult] = compte.get(ls*mult, 0) + 1
        mult+=1

nb_one = 0
for ll in compte :
    if compte[ll] == 1 :
        nb_one+=1
print(nb_one)
a=0