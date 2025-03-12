

nb = 0
for k in range(1,1000001):

    sk = str(k)
    if len(sk) % 2 == 0 :
        left = sk[:len(sk)//2]
        right = sk[len(sk)//2:]
    else :
        left = sk[:len(sk) // 2]
        right = sk[1+(len(sk) // 2):]

    right = right[-1::-1]
    if left == right :
        bk = bin(k)
        bk = bk[2:]
        if len(bk) % 2 == 0:
            left = bk[:len(bk) // 2]
            right = bk[len(bk) // 2:]
        else:
            left = bk[:len(bk) // 2]
            right = bk[1 + (len(bk) // 2):]

        right = right[-1::-1]
        if left == right:
            print(k,bk)
            nb += k


print(nb)