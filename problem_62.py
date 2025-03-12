import numpy as np

n = 22
n3 = str(n**3)
n3 = [int(i) for i in n3]
current_len = 5
L = []
sL = []
while len(n3)<15:

    if len(n3) == current_len :
        sL.append(n3)
    else :
        current_len += 1
        L.append(sL)
        sL = [n3]

    n = n+1
    n3 = str(n**3)
    n3 = [int(i) for i in n3]

for sL in L[7:8] :
    Ls = []
    Ls_n = []
    for e in sL :
        e1 = np.copy(e)
        e.sort()
        if e == [0,1,2,3,3,4,5,5,6,7,8,9] :
            print(e1)
        if e in Ls :
            index = Ls.index(e)
            Ls_n[index] += 1
        else :
            Ls.append(e)
            Ls_n.append(1)
    a=0
    index = Ls_n.index(5)
    print(Ls[index])
    print(max(Ls_n))
