import math


'''
for n in range(1,10):
    continuer = True
    ind = 1
    while continuer :
        nb = int(ind*str(n))
        if nb < ind*math.factorial(n) :
            ind += 1
        else :
            continuer = False
            print(n,ind-1)
'''
max_v = -3
for k in range(1,100001):
    s = str(k)
    v = 0
    for ss in s:
        v+= math.factorial(int(ss))
    if v == k :
        max_v += k

print(max_v)