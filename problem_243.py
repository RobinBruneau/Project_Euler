import numpy as np

import eulerlib, fractions

l_premiers = [2,3,5,7]

max_v = 2000000
n = 11
continuer= True
while continuer :

    racine = int(np.sqrt(n))

    is_premier = True
    ind = 0
    while l_premiers[ind] <= racine and is_premier:
        reste = n % l_premiers[ind]
        if reste ==  0 :
            is_premier = False
        ind+=1

    if is_premier :
        l_premiers.append(n)


    n+=2
    if n >= max_v :
        continuer = False


dict_div = {}

decompo_prem = [[],[]]

def div_premier(n,l_premiers):

    l=[]
    k=0
    while n != 1 :
        reste = n%l_premiers[k]
        nb = 0
        while reste == 0 :
            n /= l_premiers[k]
            nb+=1
            reste = n%l_premiers[k]
        if nb != 0:
            l.append(l_premiers[k])
        k+=1

    return l
'''
continuer = True
n=2
L_div_prem = []

while continuer :
    if n%1000 == 0 :
        print(n)
    div_prem = div_premier(n,l_premiers)

    if n%2 == 0 and n%3 == 0 :
        L = []
        for value in div_prem :
            if str(value) in dict_div.keys() :
                L.extend(dict_div[str(value)])
        L = set(L)
        coef = (n - 1 - len(L)) / (n - 1)
        if coef < 15499 / 94744.0:
            print(n)
            continuer = False
    
    for value in div_prem:
        if str(value) in dict_div.keys():
            dict_div[str(value)].append(n)
        else :
            dict_div.update({str(value):[n]})


    n+=1
'''
n=892371480
continuer = True
for n in range(210,210+1):
    if n%1000 == 0 :
        print(n)
    if n%1 == 0 :
        div_prem = div_premier(n,l_premiers)
        print(div_prem)
        print(n)
        v = 0
        m = 1
        for d in div_prem :
            v += n/d -1
        print(v)
        if len(div_prem) > 1 :
            for k in range(len(div_prem)):
                for j in range(k+1,len(div_prem)):
                    v-= n/(div_prem[k]*div_prem[j]) - 1

        print(v)

        coef =  1 - v/(n-1)
        print(coef)
        print("")
        if coef < 15499/94744.0 :
            continuer = False
            print(n)

    n+=1



for k in range(2,100):
    print(k,div_premier(k,l_premiers))