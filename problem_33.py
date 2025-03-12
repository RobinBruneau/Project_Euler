from tools import *
num = 1
dem = 1
for k in range(10,100):
    for j in range(k+1,100):
        frac = k/j
        lk = list(str(k))
        lj = list(str(j))
        for kk in range(2):
            for jj in range(2):
                if lk[kk] == lj[jj]:
                    if k%10 != 0 :
                        if int(lj[(jj+1)%2]) != 0 :
                            if int(lk[(kk+1)%2])/int(lj[(jj+1)%2]) == frac :
                                print(k,j)
                                num *= k
                                dem *= j
l_premiers = nombres_premiers_inf_k(max(num,dem)//100)
decomp_premier_num = div_premier(num,l_premiers)
div_num = diviseur_n(num,decomp_premier_num)

decomp_premier_dem = div_premier(dem,l_premiers)
div_dem = diviseur_n(dem,decomp_premier_dem)
div_num.sort()
div_dem.sort()
print(div_num)
print(div_dem)

for e in div_num :
    if e in div_dem :
        print(e,num/e,dem/e)