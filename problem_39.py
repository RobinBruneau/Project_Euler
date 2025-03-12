

lp = []
for p in range(1,1001):
    if p%100==0 :
        print(p)
    np = 0
    visited = []
    for c in range(1,int(p/2)):
        for a in range(1,c):
            b = p-c-a
            if c**2 == a**2+b**2 :
                l = [a,b]
                l.sort()
                if l not in visited :
                    #np.append((a,b,c))
                    np+=1
                    visited.append(l)
    lp.append(np)

print(lp.index(max(lp))+1)