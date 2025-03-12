import numpy as np
import copy

def combinaison_n(l_nb,l_choix):

    if len(l_choix) != 0 :
        all_results = []
        for choix in l_choix :
            new_l_nb = []
            for nb in l_nb :
                new_l_nb.append(nb+choix)
            new_l_choix = copy.deepcopy(l_choix)
            new_l_choix.remove(choix)
            result = combinaison_n(new_l_nb,new_l_choix)
            all_results  = all_results + result

        return all_results

    else :
        return l_nb


a= combinaison_n([""],["0","1","2","3","4","5","6","7","8","9"])
print(a[999999])