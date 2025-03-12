from tqdm import tqdm
import numpy as np

ll = []
for n in range(1,10001):
    l = []
    #for x in range(int(np.ceil(n/2 - n/np.sqrt(2))),int(np.floor(n/2 + n/np.sqrt(2)))+1):
    for x in range(1, int(np.floor(n / 2))):
        a=0
        y = np.sqrt(n*n/2 - (x-n/2)**2)+n/2
        y2 = -np.sqrt(n*n/2 - (x-n/2)**2)+n/2
        if int(y) == y :
            l.append([x,y])
            l.append([x,y2])
            l.append([x, y])
            l.append([x, y2])
            l.append([x, y])
            l.append([x, y2])
            l.append([x, y])
            l.append([x, y2])
    y = np.sqrt(n * n / 2 - ( - n / 2) ** 2) + n / 2
    y2 = -np.sqrt(n * n / 2 - ( - n / 2) ** 2) + n / 2
    if int(y) == y:
        l.append([0, y])
        l.append([0, y])
        l.append([0, y])
        l.append([0, y])

    x = int(np.floor(n / 2))
    y = np.sqrt(n * n / 2 - (x - n / 2) ** 2) + n / 2
    y2 = -np.sqrt(n * n / 2 - (x - n / 2) ** 2) + n / 2
    if int(y) == y:
        if n%2 == 0 :
            for k in range(4):
                l.append([])
        else :
            for k in range(8):
                l.append([])


    if len(l) not in ll :
        ll.append(len(l))

print(ll)