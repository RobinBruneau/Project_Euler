from tools import *


def is_tronc_prem(premier,l_premiers):
    number = str(premier)
    for k in range(len(number)-1):
        int_l = int(number[k+1:])
        int_r = int(number[:-1-k])
        if not int_l in l_premiers :
            return False
        if not int_r in l_premiers :
            return False
    return True

sum = 739397 # dernier
l_premiers = k_nombres_premiers(1000) #100000 pour le dernier
for premier in l_premiers :
    if premier > 7 and is_tronc_prem(premier,l_premiers):
        print(premier)
        sum+= premier

print(sum)