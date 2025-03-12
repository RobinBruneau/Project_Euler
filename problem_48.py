from tqdm import tqdm

def add(l1,l2):
    lf = []
    total = max(len(l1),len(l2))
    diff = len(l1)-len(l2)
    if diff > 0 :
        l2 = l2 + diff*[0]
    else :
        l1 = l1 + (-diff)*[0]

    reste = 0
    for k in range(total):
        val = l1[k]+l2[k]+reste
        if val >=10 :
            reste = val//10
            div = val%10
        else :
            div = val
            reste = 0

        lf.append(div)
    if reste != 0:
        lf.append(reste)
    return lf

sum = []
for n in tqdm(range(1,1001)):
    L = [1]
    for j in range(n):

        reste = 0
        for k,e in enumerate(L[:11]) :
            v = str(n*e+reste)
            if len(v) == 1 :
                L[k] = int(v)
                reste = 0
            else :
                reste = int(v[:-1])
                L[k] = int(v[-1])
        reste = str(reste)
        if reste != "0":
            for m in range(len(reste)):
                L.append(int(reste[-1-m]))

    sum = add(sum,L)

print(sum[9],sum[8],sum[7],sum[6],sum[5],sum[4],sum[3],sum[2],sum[1],sum[0])