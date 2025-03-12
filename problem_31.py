import numpy as np
import numpy.matlib
l_200 = 1
l_choix = [[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]]
l_choix = np.array(l_choix)
l_poids = np.array([200,100,50,20,10,5,2,1])
while len(l_choix) != 0 :
    print(l_choix.shape[0],l_200)
    l_new_choix = np.matlib.repmat(l_choix, 7, 1)
    lc = l_choix.shape[0]
    for k in range(7):
        l_new_choix[k*lc:(k+1)*lc,k+1] += 1

    l_new_choix = np.unique(l_new_choix, axis=0)
    l_new_choix_poids = np.sum(l_new_choix*l_poids,axis=1)

    ind_200 = np.where(l_new_choix_poids==200)
    l_200 += len(ind_200[0])
    ind_del = np.where(l_new_choix_poids>=200)

    l_choix = np.delete(l_new_choix, ind_del, 0)
    a=0
print(l_200)