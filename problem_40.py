

nb = 0
value = 1
rem_nb = [1,10,100,1000,10000,100000,1000000]
value_rem = []
while nb <= 1000000 :
    if nb == rem_nb[0]:
        value_rem.append(value_str[-1])
        rem_nb = rem_nb[1:]

    value_str = str(value)
    value_len = len(value_str)

    nb_new = nb + value_len

    if nb_new > rem_nb[0]:
        value_rem.append(value_str[rem_nb[0]-nb-1])
        rem_nb = rem_nb[1:]

    nb = nb_new
    value += 1

print(value_rem)
prod = 1
for e in value_rem :
    prod *= int(e)
print(prod)