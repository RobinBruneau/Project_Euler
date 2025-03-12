
from tqdm import tqdm

nb_Lychrel = 0
for k in tqdm(range(1,10000)):

    it = 1
    is_Lychrel = True
    nb = str(k)
    while is_Lychrel and it < 50 :

        nb = str(int(nb) + int(nb[-1::-1]))
        if len(nb) % 2 == 0 :
            left = nb[:len(nb)//2]
            right = nb[len(nb)//2:]
        else :
            left = nb[:len(nb) // 2]
            right = nb[1+(len(nb) // 2):]

        if left == right[-1::-1]:
            is_Lychrel = False

        it += 1

    if is_Lychrel :
        nb_Lychrel+=1

print(nb_Lychrel)