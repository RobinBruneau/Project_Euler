import numpy as np


l = [np.array([0,0,0])]

for multi in range(10):

    nl = []
    l_doublon = []
    for v in l :
        vv = list(np.array(v)+np.array([1,0,0]))
        if vv not in nl :
            nl.append(vv)
        elif vv not in l_doublon:
            l_doublon.append(vv)
        vv = list(np.array(v) + np.array([0, 1, 0]))
        if vv not in nl:
            nl.append(vv)
        elif vv not in l_doublon:
            l_doublon.append(vv)
        vv = list(np.array(v) + np.array([0, 0, 1]))
        if vv not in nl:
            nl.append(vv)
        elif vv not in l_doublon:
            l_doublon.append(vv)

    for v in l_doublon:
        nl.remove(v)

    val = (multi+1)*2+1
    deja = len(nl)
    print(nl)
    print(deja,len(l_doublon),val-deja)

    for k in range(val-deja):
        nl.append(l_doublon[k])
    l = np.copy(nl)
    print(l)
    print("")
    a=0
