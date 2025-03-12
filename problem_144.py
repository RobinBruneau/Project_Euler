import numpy as np
d = np.array([0,10.1])
p = np.array([1.4,-9.6])
rebond = 1

continuer = True

while continuer :

    pd = d-p
    v = np.array([1,p[1]/(4*p[0])])
    nd = 2*((np.dot(pd,v)*v/(np.linalg.norm(v)**2))+p)-d
    v_refl = nd-p
    v_refl /= v_refl[0]
    a = v_refl[1]
    b = p[1]-a*p[0]

    delta = 4*a*a*b*b - 4*(4+a*a)*(b*b-100)

    r1 = (-2*a*b - np.sqrt(delta)) / (8+2*a*a)
    r2 = (-2*a*b + np.sqrt(delta)) / (8+2*a*a)

    d = np.copy(p)
    if abs(r1-p[0])< 1e-5 :
        p = [r2,a*r2+b]
    else :
        p = [r1,a*r1+b]

    if p[1] >= 0 and p[0] >= -0.01 and p[0] <= 0.01 :
        continuer = False
    else :
        rebond += 1

print(rebond)
