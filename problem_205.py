import numpy as np

l4 = np.array([0 for i in range(36)])
l4[[0,1,2,3]] = 1
for k in range(8):
    l44 = np.array([0 for i in range(36)])
    for i,e in enumerate(l4) :
        if l4[i] != 0 :
            for j in range(1,5):
                l44[i+j] = l44[i+j] + l4[i]
    l4 = np.copy(l44)

l6 = np.array([0 for i in range(36)])
l6[[0,1,2,3,4,5]] = 1
for k in range(5):
    l66 = np.array([0 for i in range(36)])
    for i,e in enumerate(l6) :
        if l6[i] != 0 :
            for j in range(1,7):
                l66[i+j] = l66[i+j] + l6[i]
    l6 = np.copy(l66)



s4 = float(np.sum(l4))
s6 = float(np.sum(l6))
print(l4)
print(l6)
p = s4*s6

nb = 0
for k,e in enumerate(l4) :
    if l4[k] != 0:
        print(l4[k], np.sum(l6[:k]))
        nb += float(l4[k])*float(np.sum(l6[:k]))

nb /= p
a=0
print(nb)