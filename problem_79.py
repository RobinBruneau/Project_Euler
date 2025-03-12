

f=open("problem_79.txt",'r')

L0 = []
L_avant = [[],[],[],[],[],[],[],[],[],[]]
for line in f :
    code = line.split("\n")[0]
    L_avant[int(code[1])].append(code[0])
    L_avant[int(code[2])].append(code[1])
    L0.append(code[0])
f.close()
for k in range(len(L_avant)):
    L_avant[k] = list(set(L_avant[k]))
L0 = list(set(L0))
print(L0)
L_avant[4] = [None]
L_avant[5] = [None]


def find_vide(l):
    for k in range(len(l)):
        if l[k] == []:
            return k
def remove_e(l,e):
    for k in range(len(l)):
        if e in l[k]:
            l[k].remove(e)
    return l

def check_finish(l):
    for k in range(len(l)):
        if l[k] != [None] :
            return True
    return False

continuer = True
code_full = ""
while continuer :
    ind = find_vide(L_avant)
    L_avant[ind] = [None]
    code_full += str(ind)
    L_avant = remove_e(L_avant,str(ind))
    continuer = check_finish(L_avant)

print(code_full)
print(L_avant)