from tools import *

sum = 0
for a in range(1,100):
    print(a)
    for b in range(1,100):
        p = power(a,b)
        sum_a_b = np.sum(p)
        if sum_a_b > sum :
            sum = sum_a_b
print(sum)