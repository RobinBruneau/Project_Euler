from tqdm import tqdm

L1 = [1]
L89 = []

def suite(k):

    v = list(str(k))
    val = [int(e)**2 for e in v]
    val = sum(val)
    l = [k]
    while val != 1 and val != 89 :
        #l.append(val)
        v = list(str(val))
        val = [int(e) ** 2 for e in v]
        val = sum(val)

    if val == 1 :
        return (False,l)
    else :
        return (True,l)



nb = 0
for k in tqdm(range(2,100001)):
    #if k in L1 :
    #    a=0
    #elif k in L89 :
    #    nb+=1
    #else :
    end89,l = suite(k)
    if end89 :
        nb+=1
        #L89 = list(set(L89+l))
    else :
        a=0
        #L1 = list(set(L1+l))

print(nb)
print(suite(10000000))