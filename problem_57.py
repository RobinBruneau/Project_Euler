from tools import *


num = 7
denom = 5
sup = 0
for k in range(3,1001):
    new_num = 2*denom+num
    new_denum = num+denom



    num = new_num
    denom = new_denum
    if len(str(num))>len(str(denom)):
        sup += 1
    print(new_num,new_denum,num/denom)

print(sup)