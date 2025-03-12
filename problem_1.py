import numpy


sum = 0
for k in range(1000):
    if k%3 == 0 or k%5 == 0 :
        sum += k
print(sum)