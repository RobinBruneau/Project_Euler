


e = [2,1]
for k in range(1,34):
    e = e+ [2*k,1,1]

e = e[:100]

sup = (len(e)-1)*[1]
inf = e
for f in range(len(sup)-1):
    supm1 = sup[-1]
    infm1 = inf[-1]
    infm2 = inf[-2]
    sup = sup[:-1]
    inf = inf[:-1]
    inf[-1] = infm2*infm1+supm1
    sup[-1] = infm1

sup = inf[0]*inf[1]+sup[0]
inf = inf[1]
sup = list(str(sup))
sum_sum = sum([int(e) for e in sup])
print(sum_sum)