

max_pandigital = 0
for k in range(1000,10000):
    v = ""
    for j in range(1,3):
        v+=str(j*k)

    vv = list(v)
    cont_v = list(set(vv))
    if (len(vv) == 9) and (len(cont_v) == len(vv)) and ("0" not in vv):
        max_pandigital = max(max_pandigital,int(v))

for k in range(100,1000):
    v = ""
    for j in range(1,4):
        v+=str(j*k)

    vv = list(v)
    cont_v = list(set(vv))
    if (len(vv) == 9) and (len(cont_v) == len(vv)) and ("0" not in vv):
        max_pandigital = max(max_pandigital,int(v))

for k in range(10,100):
    v = ""
    for j in range(1,5):
        v+=str(j*k)

    vv = list(v)
    cont_v = list(set(vv))
    if (len(vv) == 9) and (len(cont_v) == len(vv)) and ("0" not in vv):
        max_pandigital = max(max_pandigital,int(v))


for k in range(1,10):
    for max_n in range(6,10):
        v = ""
        for j in range(1,max_n):
            v+=str(j*k)

        vv = list(v)
        cont_v = list(set(vv))
        if (len(vv) == 9) and (len(cont_v) == len(vv)) and ("0" not in vv):
            max_pandigital = max(max_pandigital,int(v))

print(max_pandigital)