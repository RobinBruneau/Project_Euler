from tools import *
import copy


def get_4digit_f(f):
    k = 0
    L = []
    for p in range(100):
        L.append([])
    while True :
        r = f(k)
        if r>9999 :
            return L

        if r>999 :
            p1 = int(str(r)[:2])
            p2 = int(str(r)[2:])
            if p2 >=10 :
                L[p1].append([p1,p2,r])

        k+= 1

def f_triangle(k):
    return k*(k+1)//2

def f_square(k):
    return k*k

def f_pentagonal(k):
    return k*(3*k-1)//2

def f_hexagonal(k):
    return k*(2*k-1)

def f_heptagonal(k):
    return k*(5*k-3)//2

def f_octogonal(k):
    return k*(3*k-2)

l3 = get_4digit_f(f_triangle)
l4 = get_4digit_f(f_square)
l5 = get_4digit_f(f_pentagonal)
l6 = get_4digit_f(f_hexagonal)
l7 = get_4digit_f(f_heptagonal)
l8 = get_4digit_f(f_octogonal)

all = [l3,l4,l5,l6,l7,l8]

ind_visit_1 = [1, 2, 3, 4, 5]
for sl in l3 :
    for digit_1 in sl :
        # digit 1
        d1_p1 = digit_1[0]
        d1_p2 = digit_1[1]
        d1 = digit_1[2]

        for ind_follower_1 in ind_visit_1 :
            ind_visit_2 = copy.copy(ind_visit_1)
            ind_visit_2.remove(ind_follower_1)

            for digit_2 in all[ind_follower_1][d1_p2]:
                #digit 2
                d2_p1 = digit_2[0]
                d2_p2 = digit_2[1]
                d2 = digit_2[2]

                for ind_follower_2 in ind_visit_2:
                    ind_visit_3 = copy.copy(ind_visit_2)
                    ind_visit_3.remove(ind_follower_2)

                    for digit_3 in all[ind_follower_2][d2_p2]:
                        # digit 3
                        d3_p1 = digit_3[0]
                        d3_p2 = digit_3[1]
                        d3 = digit_3[2]

                        for ind_follower_3 in ind_visit_3:
                            ind_visit_4 = copy.copy(ind_visit_3)
                            ind_visit_4.remove(ind_follower_3)

                            for digit_4 in all[ind_follower_3][d3_p2]:
                                # digit 4
                                d4_p1 = digit_4[0]
                                d4_p2 = digit_4[1]
                                d4 = digit_4[2]

                                for ind_follower_4 in ind_visit_4:
                                    ind_visit_5 = copy.copy(ind_visit_4)
                                    ind_visit_5.remove(ind_follower_4)

                                    for digit_5 in all[ind_follower_4][d4_p2]:
                                        # digit 5
                                        d5_p1 = digit_5[0]
                                        d5_p2 = digit_5[1]
                                        d5 = digit_5[2]

                                        for ind_follower_5 in ind_visit_5:
                                            ind_visit_6 = copy.copy(ind_visit_5)
                                            ind_visit_6.remove(ind_follower_5)

                                            #print(ind_follower_5)
                                            #print(digit_5,d5_p2)
                                            for digit_6 in all[ind_follower_5][d5_p2]:
                                                # digit 6
                                                d6_p1 = digit_6[0]
                                                d6_p2 = digit_6[1]
                                                d6 = digit_6[2]

                                                if d6_p2 == d1_p1 :
                                                    print(digit_1)
                                                    print(digit_2)
                                                    print(digit_3)
                                                    print(digit_4)
                                                    print(digit_5)
                                                    print(digit_6)
                                                    print(d1+d2+d3+d4+d5+d6)



a=0