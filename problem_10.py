import numpy as np

l_premiers = [2,3,5,7]

n = 11
continuer= True
sum = 0
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
        sum += n

    n+=2
    if n >= 2000000 :
        continuer = False

print(len(l_premiers))
print(sum+2+3+5+7)


m=3
Li=[2]
sum = 2
while m<2000000:
    a=0
    j=0
    racine = int(np.sqrt(m))
    while a==0 and Li[j]<=racine:

        reste = m%Li[j]
        if reste==0:
            a=1
        j+=1
    if a==0:
        Li.append(float(m))
        sum += m
    m+=2
print(len(Li))
print(np.sum(Li))
print(sum)