import numpy
from tools import *

def abundant_number(n,div):
    return n<sum(div[:-1])


l_premiers = nombres_premiers_inf_k(28123)
all_abundant = []
for n in range(1,28123):
    div_p = div_premier(n,l_premiers)
    div = diviseur_n(n,div_p)
    is_abundant = abundant_number(n,div)
    if is_abundant :
        all_abundant.append(n)

list_not_sum_of_two = []
for n in range(1,28123):
    if n%100 ==0 :
        print(n)
    max_range = min(len(all_abundant),(n/2)+1)
    is_sum_of_two = False
    it = 0
    while (not is_sum_of_two) and it<max_range:

        second = n - all_abundant[it]
        if second in all_abundant :
            is_sum_of_two = True
        it+=1

    if (not is_sum_of_two) :
        list_not_sum_of_two.append(n)
print(sum(list_not_sum_of_two))
