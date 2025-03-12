

l = [0,1,1,0]
sup_million = 0
for k in range(2,101):
    ll = [0,]
    for i in range(len(l)-1):
        val = l[i]+l[i+1]
        if val > 1000000 :
            sup_million += 1
        ll.append(val)
    ll.append(0)
    l = ll
print(sup_million)