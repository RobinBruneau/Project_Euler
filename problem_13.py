import numpy as np

f= open("problem_13.txt",'r')
l = []
for line in f:
    line = line.split("\n")[0]
    line = list(line)
    line = [int(e) for e in line]
    l.append(line)
tab = np.array(l)


val_sum = []

reste = 0
for k in range(50):
    val = tab[:,-1-k]
    sum = np.sum(val)
    sum += reste

    sum_char = str(sum)

    val_sum.append(int(sum_char[-1]))
    reste = int(sum_char[:-1])
val_sum.append(reste)
a=0

str_finakl = ""
for k in range(len(val_sum)):
    str_finakl += str(val_sum[-1-k])

print(str_finakl[:10])


