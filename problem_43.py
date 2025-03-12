
import copy

div2 = [0,2,4,6,8]
div5 = [0,5]

l_pandigital = []
choice = [0,1,2,3,4,5,6,7,8,9]
for p4 in div2 :

    if p4 == 0 :
        choice_p6 = [5]
    else :
        choice_p6 = [0,5]
    for p6 in choice_p6 :
        choice_p3 = [0,1,2,3,4,5,6,7,8,9]
        choice_p3.remove(p4)
        choice_p3.remove(p6)
        for p3 in choice_p3 :
            choice_p5 = [0,1,2,3,4,5,6,7,8,9]
            choice_p5.remove(p4)
            choice_p5.remove(p6)
            choice_p5.remove(p3)
            for p5 in choice_p5 :
                if (p3+p4+p5) % 3 == 0 :
                    choice_p7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    choice_p7.remove(p4)
                    choice_p7.remove(p6)
                    choice_p7.remove(p3)
                    choice_p7.remove(p5)
                    for p7 in choice_p7 :
                        if (p7+10*p6+100*p5) % 7 == 0 :
                            choice_p8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                            choice_p8.remove(p4)
                            choice_p8.remove(p6)
                            choice_p8.remove(p3)
                            choice_p8.remove(p5)
                            choice_p8.remove(p7)
                            for p8 in choice_p8 :
                                if (p8 + 10 * p7 + 100 * p6) % 11 == 0:
                                    choice_p9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    choice_p9.remove(p4)
                                    choice_p9.remove(p6)
                                    choice_p9.remove(p3)
                                    choice_p9.remove(p5)
                                    choice_p9.remove(p7)
                                    choice_p9.remove(p8)
                                    for p9 in choice_p9:
                                        if (p9 + 10 * p8 + 100 * p7) % 13 == 0:
                                            choice_p10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                            choice_p10.remove(p4)
                                            choice_p10.remove(p6)
                                            choice_p10.remove(p3)
                                            choice_p10.remove(p5)
                                            choice_p10.remove(p7)
                                            choice_p10.remove(p8)
                                            choice_p10.remove(p9)
                                            for p10 in choice_p10:
                                                if (p10 + 10 * p9 + 100 * p8) % 17 == 0:
                                                    choice_p1 = copy.deepcopy(choice_p10)
                                                    choice_p1.remove(p10)
                                                    for p1 in choice_p1:
                                                        choice_p2 = copy.deepcopy(choice_p1)
                                                        choice_p2.remove(p1)
                                                        for p2 in choice_p2 :
                                                            l_pandigital.append(10**9*p1+10**8*p2+10**7*p3+10**6*p4+10**5*p5+10**4*p6+10**3*p7+10**2*p8+10**1*p9+p10)
print(l_pandigital)
print(sum(l_pandigital))

