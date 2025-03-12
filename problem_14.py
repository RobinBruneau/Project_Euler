from tqdm import tqdm
import numpy as np
import time
len = []
for k in tqdm(range(2,1000000)):

    l = 1
    while k != 1 :

        if k%2 == 0 :
            k = k/2
        else :
            k = 3*k+1
        l+=1
    len.append(l)


print(1+np.argmax(len))