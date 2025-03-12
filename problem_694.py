from tools import *
from tqdm import tqdm
import bisect

def l_pow_n_inf_k(n,k_pow):
    max_pow = int((k_pow*math.log(10)) // (math.log(n)))
    if max_pow>=3:
        l_pow = np.linspace(3,max_pow,max_pow-2)
        return (l_pow).astype(int)
    else :
        return np.array([])


max_v_pow = 10
l_prem = nombres_premiers_inf_k(np.ceil(10**(max_v_pow/3))+1)
l_pow_prem = []
for e in tqdm(l_prem) :
    l_pow_prem.append(l_pow_n_inf_k(e,max_v_pow))

'''
L = [math.log(1)]
max_v = max_v_pow*math.log(10)
for k in tqdm(range(len(l_prem))):
    #print(len(L))
    sL = []
    for el_p in l_pow_prem[k]:
        val = el_p*math.log(l_prem[k])
        for el_s in L :
            el_sp = el_s + val
            if el_sp < max_v:
                bisect.insort(sL,el_sp)
            else :
                break
    #print(np.exp(sL))
    L = fusion(L,sL)
'''

L = []
max_v = max_v_pow*math.log(10)
for k in tqdm(range(len(l_prem))):
    #print(len(L))
    sL = []
    val_k = math.log(l_prem[k])
    max_pow_k = int((max_v_pow * math.log(10)) // val_k)
    #print(l_prem[k],max_pow_k,l_pow_prem[k]**3)
    sL = (np.linspace(3*val_k,max_pow_k*val_k,max_pow_k-2)).tolist()
    #print(len(L))
    for el_s in L:
        nb = int((max_v - el_s) // val_k)
        if nb > 2 :
            sLL = (np.linspace(el_s+3*val_k,el_s+nb*val_k,nb-2)).tolist()
            sL = sL + sLL

    #print(np.exp(sL))
    L = L + sL
L = [math.log(1)] + L
print(len(L))
print(np.exp(L))
sumL = 0
for el in L :
    sumL += np.floor(np.exp(max_v_pow*math.log(10)-el))
print(sumL)
v = (np.round(np.exp(L))).astype(int)
#print(v)
a=0


#(10^1) = 11
#(10^2) = 126
#(10^3) = 1318
#(10^4) = 13344
#(10^5) = 133848
#(10^6) = 1339485
#(10^7) = 13397119
#(10^8) = 133976753
#(10^9) = 1339780424
#(10^10) = 13397833208
#(10^11) = 133978396859
#(10^12) = 1339784112539
#(10^13) = 13397841446161
#(10^14) = 133978415161307
#(10^15) = 1339784153146359
#(10^16) = 13397841534812404
#(10^17) = 133978415355411689