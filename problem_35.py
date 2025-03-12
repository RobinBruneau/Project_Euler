from tools import *
from tqdm import tqdm

l_premiers = nombres_premiers_inf_k(1000000)

nb_circular_prime = 0
for vv in tqdm(range(len(l_premiers))) :
    n = l_premiers[vv]
    n_str = str(n)

    is_circular_prime = True
    k=0
    while is_circular_prime and k != len(n_str) :
        n_value = int(n_str[k:]+n_str[:k])
        if n_value not in l_premiers :
            is_circular_prime = False
        k += 1
    if is_circular_prime :
        nb_circular_prime += 1

print(nb_circular_prime)