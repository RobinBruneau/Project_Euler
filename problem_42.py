
max = 0

ln = []
nb = 0
for n in range(20):
    ln.append(n*(n+1)/2)
f=open("problem_42.txt","r")
for line in f:
    names = line.split(",")
names_ = []
for name in names :
    names_.append(name[1:-1])

for name_ in names_ :
    score = 0
    for lettre in name_ :
        score += ord(lettre)-64
    if score in ln :
        nb += 1
    if score > max :
        max = score

print(max)
print(nb)

