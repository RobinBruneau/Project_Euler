f=open("problem_18.txt",'r')
L = []

for line in f :
    line = line.split("\n")[0]
    line = line.split(" ")
    L.append([int(e) for e in line])


for k in range(len(L)-1):
    sl = L[-1-k]
    slsup = L[-1-k-1]
    for i in range(len(sl)-1):
        v = max(sl[i],sl[i+1])
        slsup[i] += v

print(L[0])