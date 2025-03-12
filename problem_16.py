import numpy as np
from tqdm import tqdm

L = [1]

for j in tqdm(range(1000)):

    reste = 0
    for k,e in enumerate(L) :
        v = str(2*e+reste)
        if len(v) == 1 :
            L[k] = int(v)
            reste = 0
        else :
            reste = int(v[:-1])
            L[k] = int(v[-1])
    reste = str(reste)
    if reste != "0":
        for m in range(len(reste)):
            L.append(int(reste[-1-m]))

print(sum(L))
