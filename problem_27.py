import numpy as np

l_premiers = [2,3,5,7]

max_v = 1000
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

l_choix = []
max_val = 0
for b in l_premiers :
    for a in range(-b-1,1000):
        p = a+b+1
        if p in l_premiers :
            nb = 2
            val = 3*3+3*a+b
            while val in l_premiers :
                nb += 1
                val = (nb+1)**2+(nb+1)*a+b

            if nb > max_val :
                l_choix = [a,b]
                max_val = nb

print(l_choix[0]*l_choix[1])
