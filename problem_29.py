from tools import *
n=100
total = (n-1)*(n-1)
all_decomp_power = []
for value in range(2,n+1):
    l_premiers = nombres_premiers_inf_k(101)
    decomp = div_premier(value,l_premiers)
    for power in range(2,n+1):
        decomp_power = []
        for e in decomp :
            decomp_power.append([e[0],e[1]*power])
        if decomp_power not in all_decomp_power :
            all_decomp_power.append(decomp_power)
        a=0
print(len(all_decomp_power))