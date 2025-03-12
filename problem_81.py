import numpy as np

f=open("problem_81.txt",'r')
map = []
for line in f :
    line = line.split("\n")[0].split(",")
    line = [int(e) for e in line]
    map.append(line)
map = np.array(map)
map_plus = -1* np.ones((82,82))
map_plus[1:-1,1:-1] = map
a=0
f.close()

chemins = []
for i in range(1,81):
    for j in range(1,81):
        chemin_local = []
        if map_plus[i+1,j] != -1 :
            chemin_local.append([80*(i-1+1)+j-1,map[i-1+1,j-1]])
        if map_plus[i,j+1] != -1 :
            chemin_local.append([80 * (i-1) + j-1 + 1, map[i-1, j-1+1]])
        chemins.append(chemin_local)


deja_vu = np.zeros(6400)
distance = np.inf*np.ones(6400)
a=0

ind_depart = 0
distance[0] = map[0,0]
a=0

pas_vu = np.where(deja_vu==0)
while len(pas_vu[0]) != 0 :
    dd = distance[pas_vu]
    ind = pas_vu[0][np.argmin(dd)]
    #ind = pas_vu[0][0]
    a=0

    voisins = chemins[ind]
    deja_vu[ind] = 1

    for v in voisins :
        distance[v[0]] = min(distance[v[0]],distance[ind]+v[1])

    pas_vu = np.where(deja_vu == 0)


print(distance[6400-1])