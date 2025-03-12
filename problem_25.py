import copy

fibo_nm2 = [1]
fibo_nm1 = [1]
fibo_n = [2]

ind = 3
while len(fibo_n) < 1000 :
    fibo_nm2 = copy.copy(fibo_nm1)
    fibo_nm1 = copy.copy(fibo_n)

    fibo_n = []
    reste = 0
    if len(fibo_nm2)<len(fibo_nm1):
        fibo_nm2 += [0]*(len(fibo_nm1)-len(fibo_nm2))

    for k in range(len(fibo_nm1)):
        v = fibo_nm1[k]+fibo_nm2[k]+reste
        sv = str(v)
        fibo_n+= [int(sv[-1])]
        if len(sv)>1 :
            reste = int(sv[:-1])
        else :
            reste = 0
    if reste != 0 :
        s_reste = str(reste)
        for k in range(len(s_reste)):
            fibo_n+=[int(s_reste[-1-k])]

    ind += 1

print(ind)
