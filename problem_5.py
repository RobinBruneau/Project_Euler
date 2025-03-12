
continuer = True
ind = 2520
while continuer :

    sum = 0
    for k in range(1,21):
        sum += ind%k

    if sum == 0 :
        print(ind)
        continuer = False

    ind +=1