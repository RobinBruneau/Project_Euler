import numpy as np


def f(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10



A = np.ones((11,11))
B = np.zeros((11,1))
for k in range(1,12):
    for j in range(1,11):
        A[k-1,j] = k**j
    B[k-1] = f(k)
a=0

val = []
for k in range(10):

    sA = A[:k+1,:k+1]
    sB = B[:k+1]

    x = np.round(np.linalg.solve(sA, sB))

    val.append(np.dot(A[k+1,:k+1],x)[0])
    a=0
a=0
print(np.sum(val))

