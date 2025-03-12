import numpy as np
import bisect
import math

def in_list(l, e):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(l, e)
    if i:
        return l[i-1] == e
    else :
        return False


def primes_below(k):
    """
    Computes the list of prime numbers less than k.

    Parameters:
    k (int): The upper limit (exclusive).

    Returns:
    list: A list of prime numbers less than k.
    """
    if k < 2:
        return []

    sieve = [True] * k
    sieve[0] = sieve[1] = False

    for i in range(2, int(k ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, k, i):
                sieve[multiple] = False

    return [i for i, is_prime in enumerate(sieve) if is_prime]


def k_nombres_premiers(k):

    l_premiers = [2,3,5,7]

    n = 11
    continuer= True
    while continuer :

        racine = int(np.sqrt(n))

        is_premier = True
        ind = 0
        while l_premiers[ind] <= racine and is_premier:
            reste = n % l_premiers[ind]
            if reste ==  0 :
                is_premier = False
            ind+=1

        if is_premier :
            l_premiers.append(n)


        n+=2
        if len(l_premiers) == k :
            continuer = False

    return l_premiers

def nombres_premiers_inf_k(k):
    powa = 1
    check_3 = 0
    check_5 = 0
    check_7 = 4
    l_premiers = [2, 3, 5, 7, 11, 13]
    max_v = k
    n = 15
    continuer = True
    it = 0
    if l_premiers[-1] > k :
        for ind in range(len(l_premiers)):
            if l_premiers[ind] > k :
                return l_premiers[:ind]

    while continuer:

        if check_3 == 3 or check_5 == 5 or check_7 == 7 :
            rien = 0

        else :
            if is_prime(n):
                l_premiers.append(n)

        n += 2
        it += 1

        check_3 = (check_3 + 1) % 3
        check_5 = (check_5 + 1) % 5
        check_7 = (check_7 + 1) % 7

        if n>10**powa :
            print("_____10^{}".format(powa))
            powa +=1
        if n >= max_v:
            continuer = False

    return l_premiers

def div_premier(n,l_premiers):

    l=[]
    k=0
    while n != 1 :
        reste = n%l_premiers[k]
        nb = 0
        while reste == 0 :
            n /= l_premiers[k]
            nb+=1
            reste = n%l_premiers[k]
        if nb != 0:
            l.append([l_premiers[k],nb])
        k+=1

    return l


def prime_decomposition(primes, k):
    """
    Decomposes k into its prime factors using the given list of prime numbers.

    Parameters:
    primes (list): A list of prime numbers.
    k (int): The number to be decomposed.

    Returns:
    dict: A dictionary with prime factors as keys and their exponents as values.
    """
    factorization = {}
    for p in primes:
        while k % p == 0:
            factorization[p] = factorization.get(p, 0) + 1
            k //= p
        if k == 1:
            break
    return factorization


def diviseur_n(n,decomp_prem):

    list_diviseur = recursive_multip_decomp([1],decomp_prem)
    return list_diviseur



def recursive_multip_decomp(result,decomp_premier):

    if len(decomp_premier) != 0 :
        prem = decomp_premier[0][0]
        nb = decomp_premier[0][1]
        new_results = []
        for val in result :
            for n in range(nb+1) :
                new_results.append(val*(prem**n))

        return recursive_multip_decomp(new_results,decomp_premier[1:])

    return result


def add(l1,l2):
    lf = []
    total = max(len(l1),len(l2))
    diff = len(l1)-len(l2)
    if diff > 0 :
        l2 = l2 + diff*[0]
    else :
        l1 = l1 + (-diff)*[0]

    reste = 0
    for k in range(total):
        val = l1[k]+l2[k]+reste
        if val >=10 :
            reste = val//10
            div = val%10
        else :
            div = val
            reste = 0

        lf.append(div)
    if reste != 0:
        lf.append(reste)
    return lf


def power(n,k):
    L = [1]
    for j in range(k):
        reste = 0
        for k,e in enumerate(L) :
            v = str(n*e+reste)
            if len(v) == 1 :
                L[k] = int(v)
                reste = 0
            else :
                reste = int(v[:-1])
                L[k] = int(v[-1])
            a=0
        reste = str(reste)
        if reste != "0":
            for m in range(len(reste)):
                L.append(int(reste[-1-m]))
    return L

def power2(a,b):

    l1 = [1]
    l2 = []
    for e in str(a):
        l2.append(int(e))
    l2.reverse()

    for k in range(b):
        l1 = product(l1,l2)
        a=0
    return l1


def product(l1,l2):

    def product_fast(L,n):
        Lf = [0]*len(L)
        reste = 0
        for k, e in enumerate(L):
            v = str(n * e + reste)
            if len(v) == 1:
                Lf[k] = int(v)
                reste = 0
            else:
                reste = int(v[:-1])
                Lf[k] = int(v[-1])
            a = 0
        reste = str(reste)
        if reste != "0":
            for m in range(len(reste)):
                Lf.append(int(reste[-1 - m]))
        return Lf

    prod = []
    for k,e in enumerate(l2) :
        sL = k*[0] + product_fast(l1,e)
        prod = add(prod,sL)

    return prod


def add_cmb(cmb,l_choix,depth):

    if depth == 0 :
        return [cmb]
    else :
        l_cmb = []
        for ne,e in enumerate(l_choix) :
            l_cmb = l_cmb + add_cmb(cmb+[e],l_choix[ne+1:],depth-1)

        return l_cmb

def k_parmi_n(k,n):
    return add_cmb([],np.arange(n).tolist(),k)


def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1<n1 and i2<n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1<n1:
    	L12[i] = L1[i1]
    	i1 += 1
    	i += 1
    while i2<n2:
    	L12[i] = L2[i2]
    	i2 += 1
    	i += 1
    return L12


def tri_fusion_recursif(L):
    n = len(L)
    if n > 1:
        p = int(n / 2)
        L1 = L[0:p]
        L2 = L[p:n]
        tri_fusion_recursif(L1)
        tri_fusion_recursif(L2)
        L[:] = fusion(L1, L2)


def tri_fusion(L):
    M = list(L)
    tri_fusion_recursif(M)
    return M

