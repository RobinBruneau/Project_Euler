import numpy as np
from tools import *
from tqdm import tqdm
kk=5

def is_valid(l1,l2):
    nb = int(str(l1) + str(l2))
    nb2 = int(str(l2) + str(l1))
    return is_prime(nb) and is_prime(nb2)

l_premiers = nombres_premiers_inf_k(10000)

for p1 in tqdm(range(len(l_premiers))):
    pp1 = l_premiers[p1]
    for p2 in range(p1+1,len(l_premiers)):
        pp2 = l_premiers[p2]
        if is_valid(pp1,pp2):

            for p3 in range(p2+1,len(l_premiers)):
                pp3 = l_premiers[p3]
                if is_valid(pp1,pp3) and is_valid(pp2,pp3):

                    for p4 in range(p3+1,len(l_premiers)) :
                        pp4 = l_premiers[p4]

                        if is_valid(pp1,pp4) and is_valid(pp2,pp4) and is_valid(pp3,pp4):

                            for p5 in range(p4+1,len(l_premiers)):
                                pp5 = l_premiers[p5]

                                if is_valid(pp1,pp5) and is_valid(pp2,pp5) and is_valid(pp3,pp5) and is_valid(pp4,pp5):
                                    print(pp1,pp2,pp3,pp4,pp5)
                                    print(pp1+pp2+pp3+pp4+pp5)
