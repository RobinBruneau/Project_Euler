import math
from tqdm import tqdm

def sum_fact(n):
    #print(n,sum([math.factorial(int(k)) for k in str(n)]))
    return sum([math.factorial(int(k)) for k in str(n)])

def chain_len(n):
    stop1 = [169, 363601, 1454]
    stop2 = [45361,45362, 871, 872]
    if n in stop1 :
        return 3
    if n in stop2 :
        return 2
    else:
        sf = sum_fact(n)
        if sf == n:
            return 1
        else :
            return 1 + chain_len(sum_fact(n))

nb_chain_60 = 0
for k in tqdm(range(3,1000000)):
    if chain_len(k) == 60 :
        nb_chain_60 += 1
print(nb_chain_60)