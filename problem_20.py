

L = [1]
val = 100
for k in range(2,val+1):
    reste = 0
    for i in range(len(L)):
        v = str(L[i]*k+reste)
        L[i] = int(v[-1])
        r = v[:-1]
        if r == "" :
            reste = 0
        else :
            reste = int(v[:-1])

    if reste != 0 :
        reste = str(reste)
        for l in range(len(reste)) :
            L.append(int(reste[-1-l]))

print(sum(L))

