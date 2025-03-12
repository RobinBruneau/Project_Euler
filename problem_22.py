import numpy as np

f=open("problem_22.txt",'r')
position = 1
sum = 0
for line in f:
    names = line.split(",")
names_ = []
for name in names :
    names_.append(name[1:-1])


names_.sort()
for name_ in names_ :
    score = 0
    for lettre in name_ :
        score += ord(lettre)-64
    sum += position * score
    position += 1

print(sum)