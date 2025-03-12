import numpy as np

sum_power_5 = 0
for k in range(2,1000000):
    sum = np.sum(np.array(list(str(k))).astype(int)**5)
    if sum == k :
        print(k)
        sum_power_5 += k

print(sum_power_5)