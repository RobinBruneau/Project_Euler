

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

all_sum = [1]
for val in [3,5,7,9]:

    sum = [val]
    prev_value = [val]
    prev_add = [val-1]
    for k in range(499):
        prev_add =  add(prev_add,[8])

        prev_value = add(prev_value,prev_add)
        #print(prev_add,prev_value)
        sum = add(sum,prev_value)

    all_sum = add(all_sum,sum)

s=""
for k in range(len(all_sum)):
    s += str(all_sum[-1-k])
print(s)