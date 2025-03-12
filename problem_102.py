import numpy as np
import matplotlib.pyplot as plt

def isInTriangle(a,b,c,p):

    pa = a-p
    pb = b-p
    pc = c-p
    ab = b-a
    ac = c-a
    bc = c-b

    c1 = np.cross(pa,pb)
    c2 = np.cross(pa,pc)
    c3 = np.cross(pc,pb)

    if c1 == 0 :
        print("*")
        return False
    if c2 == 0 :
        print("*")
        return False
    if c3 == 0 :
        print("*")
        return False

    aire1 = np.linalg.norm(np.cross(pb,pc))
    aire2 = np.linalg.norm(np.cross(pc,pa))
    aire3 = np.linalg.norm(np.cross(pa,pb))
    aireTot = np.linalg.norm(np.cross(ab,ac))

    alpha = aire1/aireTot
    beta = aire2/aireTot
    gamma = aire3/aireTot

    #if aire1+aire2+aire3 == aireTot:
    #if alpha+beta+gamma == 1:
    if alpha>=0 and alpha <=1.0 and beta>= 0.0 and beta <= 1.0 and gamma>=0.0 and gamma <=1.0 and aire1+aire2+aire3 == aireTot:
        return True
    else :
        return False


f=open("problem_102.txt","r")
p = np.array([0.0,0.0])
sum = 0
for line in f :
    line = line.split("\n")[0].split(",")

    a = np.array([float(line[0]),float(line[1])])
    b = np.array([float(line[2]),float(line[3])])
    c = np.array([float(line[4]),float(line[5])])

    if isInTriangle(a,b,c,p) :
        sum += 1
    else :
        #print(a,b,c)
        #print(line)
        #plt.figure()
        #plt.plot([a[0],b[0],c[0],a[0]],[a[1],b[1],c[1],a[1]])
        #plt.plot([p[0]],[p[1]],"x")
        #plt.show()
        a=0
print(sum)
