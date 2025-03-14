import random
from tqdm import tqdm
import numpy as np

def next_in_list(value,l):
    for k in range(len(l)-1):
        if value > l[k] and value < l[k+1] :
            return l[k+1]
    return l[0]

monopoly_cases_count = [0 for k in range(40)]

for parties in tqdm(range(1000)):


    list_community = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,10]
    list_chance = [-1,-1,-1,-1,-1,-1,0,10,11,24,39,5,-3,100,100,200,200]
    random.shuffle(list_community)
    random.shuffle(list_chance)

    is_triplet_duo = [False,False,False]
    case_id = 0
    rails_id = [5,15,25,35]
    utility_id = [12,28]
    for k in range(100000):
        de1 = random.randint(1,4)
        de2 = random.randint(1,4)
        is_triplet_duo = [de1==de2]+is_triplet_duo[:2]
        if sum(is_triplet_duo) == 3 :
            case_id = 10
            monopoly_cases_count[case_id] += 1
            is_triplet_duo = [False, False, False]
        else :
            total = de1+de2
            case_id = (case_id+total)%40


            if case_id in [2,17,33] :
                action = list_community[0]
                list_community = list_community[1:]+[list_community[0]]
                if action != -1 :
                    case_id = action
                    if case_id == 10 :
                        is_triplet_duo = [False, False, False]
                    monopoly_cases_count[case_id] += 1
                else :
                    monopoly_cases_count[case_id] += 1


            elif case_id in [7,22,36]:
                action = list_chance[0]
                list_chance = list_chance[1:] + [list_chance[0]]
                if action != -1 :

                    if action == 100 :
                        # next station
                        goto = next_in_list(case_id,rails_id)
                        case_id = goto
                        monopoly_cases_count[case_id] += 1

                    elif action == 200 :
                        # next utility
                        goto = next_in_list(case_id, utility_id)
                        case_id = goto
                        monopoly_cases_count[case_id] += 1

                    elif action == -3 :
                        case_id = (case_id-3)%40
                        if case_id == 33 :
                            action = list_community[0]
                            list_community = list_community[1:] + [list_community[0]]
                            if action != -1:
                                case_id = action
                                if case_id == 10:
                                    is_triplet_duo = [False, False, False]
                                monopoly_cases_count[case_id] += 1
                            else :
                                monopoly_cases_count[case_id] += 1
                        else :
                            monopoly_cases_count[case_id] += 1

                    else :
                        case_id = action
                        if case_id == 10 :
                            is_triplet_duo = [False, False, False]
                        monopoly_cases_count[case_id] += 1

                else :
                    monopoly_cases_count[case_id] += 1
            elif case_id == 10 :
                monopoly_cases_count[case_id] += 1
                is_triplet_duo = [False, False, False]

            # go to prison
            elif case_id == 30 :
                case_id = 10
                is_triplet_duo = [False, False, False]
                monopoly_cases_count[case_id] += 1

            else :
                monopoly_cases_count[case_id] += 1


sum_val = sum(monopoly_cases_count)
monopoly_cases_count  = [x/sum_val for x in monopoly_cases_count]
order = np.argsort(monopoly_cases_count)
for k in range(len(monopoly_cases_count)):
    print(order[-1-k],monopoly_cases_count[order[-1-k]])
a=0