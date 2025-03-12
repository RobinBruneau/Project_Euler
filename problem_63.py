import numpy as np


all_add = 0
for n in range(1,25):
    v = np.exp(np.log(10)*(n-1)/n)
    #print(n,v,np.ceil(v))

    n_add = 0
    for k in range(int(np.ceil(v)),10):
        n_add += 1
    all_add += n_add
print(all_add)