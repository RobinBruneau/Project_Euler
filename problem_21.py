import numpy as np

l_premiers = [2,3,5,7]

max_v = 200000
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
            l.append([l_premiers[k],nb])
        k+=1

    return l


continuer = True
n = 2

def ensemble(div):

    if len(div) != 0 :
        v = div[0]
        l = []
        e = ensemble(div[1:])
        l_val = []
        for k in range(v[1]+1):
            vv = [(v[0]**k)*val for val in e]
            l_val = l_val + vv
        return l_val
    else :
        return [1]


vall = 0
while continuer:

    div_prem = div_premier(n, l_premiers)
    L = []
    s = set(ensemble(div_prem))
    s = list(s)
    s.remove(n)
    sum1 = sum(s)
    div_prem = div_premier(sum1, l_premiers)
    s = set(ensemble(div_prem))
    s = list(s)
    s.remove(sum1)
    sum2 = sum(s)

    if sum2 == n and sum1 != n :
        print(n)
        vall += n
    n += 1

    if n == 10000 :
        continuer = False

print(vall)