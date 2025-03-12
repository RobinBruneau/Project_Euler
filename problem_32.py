from  tqdm import tqdm
sum = 0
l_prod = []
for a in tqdm(range(1,10000)):
    for b in range(a,10000):
        prod = a * b
        if len(str(a)+str(b)+str(prod)) == 9 :
            v = str(a)+str(b)
            vv = list(v)
            cont_v = list(set(vv))
            if len(cont_v) == len(vv):

                v += str(prod)
                vv = list(v)
                cont_v = list(set(vv))
                if (len(vv) == 9) and (len(cont_v) == len(vv)) and ("0" not in vv):
                    if prod not in l_prod :
                        sum += prod
                        print(a,b,prod)
                        l_prod.append(prod)

print(sum)