import numpy as np
from tqdm import tqdm

x = np.array([3,4,5]).reshape(3,1)


def all_reduc_tri(x,v_max):
    R1 = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
    R2 = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
    R3 = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

    x1 = R1 @ x
    x2 = R2 @ x
    x3 = R3 @ x

    if np.min(x1[:2])<=v_max :
        if np.max(x1[:2])<=2*v_max :
            x1_follow = [x1] + all_reduc_tri(x1,v_max)
        else :
            x1_follow = []
    else :
        x1_follow = []

    if np.min(x2[:2])<=v_max :
        if np.max(x2[:2]) <= 2 * v_max:
            x2_follow = [x2] + all_reduc_tri(x2,v_max)
        else :
            x2_follow = []
    else :
        x2_follow = []

    if np.min(x3[:2])<=v_max :
        if np.max(x3[:2]) <= 2 * v_max:
            x3_follow = [x3] + all_reduc_tri(x3,v_max)
        else :
            x3_follow = []
    else :
        x3_follow = []

    return x1_follow+x2_follow+x3_follow

v_max = 100
results = [np.array([3,4,5]).reshape(3,1)]+all_reduc_tri(x,v_max=v_max)

results = [[x[0][0],x[1][0],x[2][0]] for x in results]

a=0

compte = {}
total = 0
for res in tqdm(results) :
    mult = 1
    while np.min(np.array(res[:2])*mult) <= v_max and np.max(np.array(res[:2])*mult) <= 2*v_max :

        add = 0
        cmb = np.array(res) * mult
        if cmb[0]<= v_max :
            if cmb[1] <= v_max:
                add += cmb[1] // 2
            else :
                diff = cmb[1]-v_max-1
                add += (cmb[1]//2) - diff
                if (cmb[1]//2) - diff < 0 :
                    a=0
        if cmb[1] <= v_max :
            if cmb[0] <= v_max:
                add += cmb[0] // 2
            else:
                diff = cmb[0] - v_max - 1
                add += (cmb[0] // 2) - diff
                if (cmb[0] // 2) - diff < 0 :
                    a=0

        total += add
        mult+=1


print(total)