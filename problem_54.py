import copy
import numpy as np

f=open("problem_54.txt","r")
games = []
for line in f:
    data = line.split("\n")[0]
    cards = data.split(" ")
    games.append([cards[:5],cards[5:]])
a=0

def sort_by_value(cards):
    conv={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
    values = []
    occ = []
    for e in cards :
        conv_e = conv[e[0]]
        if conv_e not in values :
            values.append(conv_e)
            occ.append(1)
        else :
            ind = values.index(conv_e)
            occ[ind] += 1
    return values,occ

def sort_by_suit(cards):
    conv = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
            "A": 14}
    values = [[],[],[],[]]
    conv2={"C":0,"S":1,"D":2,"H":3}

    for e in cards:
        values[conv2[e[1]]].append(conv[e[0]])
    for k in range(4):
        values[k].sort()
    while [] in values :
        values.remove([])
    return values


def get_best_hand(cards):
    values,values_occ = sort_by_value(cards)
    if max(values_occ)==4 :
        print(True)
    suits = sort_by_suit(cards)


    final_hand = copy.copy(values)
    final_hand.sort()
    final_hand_rev = copy.copy(values)
    final_hand_rev.sort(reverse=True)
    best_hand = 0

    hand = [max(values)]

    dp = np.where(np.array(values_occ) == 2)[0]
    if 2 in values_occ :
        best_hand = 1
        hand = [values[values_occ.index(2)]]
        if 3 in values_occ :
            best_hand = 6
            hand = [values[values_occ.index(3)]] + hand


    if len(dp) == 2 :
        best_hand = 2
        hand = [values[dp[0]],values[dp[1]]]
        hand.sort(reverse=True)
        a=0

    if 3 in values_occ :
        best_hand = 3
        ind = values[values_occ.index(3)]

    if len(values) == 5 :
        if np.sum(np.array(final_hand[1:])-np.array(final_hand[:-1])) == 4 :
            best_hand = 4
            hand = [final_hand[-1]]

    if 4 in values_occ:
        best_hand = 7
        hand = [values[values_occ.index(4)]]

    if len(suits) == 1 :
        best_hand = 5
        hand = final_hand_rev
        if np.sum(np.array(final_hand[1:]) - np.array(final_hand[:-1])) == 4:
            best_hand = 8
            hand = final_hand[-1]
            if final_hand[-1] == 14 :
                best_hand = 9
                hand = final_hand_rev

    if best_hand in [2,3,4,5,6,7,8,9]:
        #print("")
        #print(best_hand,values,suits,cards)
        a=0

    return best_hand,hand,final_hand_rev

victory_p1 = 0
for game in games :
    p1_hand,p1_card,p1_all = get_best_hand(game[0])
    p2_hand,p2_card,p2_all = get_best_hand(game[1])

    if p1_hand > p2_hand :
        victory_p1 += 1
        #print("")
        #print(p1_hand, p1_card, p1_all)
        #print(p2_hand, p2_card, p2_all)
    elif p1_hand == p2_hand :
        #print("")
        #print(p1_hand,p1_card,p1_all)
        #print(p2_hand,p2_card,p2_all)
        equality = True
        ind = 0
        while equality and ind < len(p1_card):
            if p1_card[ind]>p2_card[ind]:
                victory_p1 += 1
                #print("victory")
                equality = False
            elif p1_card[ind] == p2_card[ind]:
                ind += 1
            else :
                equality = False
        if equality :
            ind = 0
            while equality and ind < len(p1_all):
                if p1_all[ind] > p2_all[ind]:
                    victory_p1 += 1
                    #print("victory")
                    equality = False
                elif p1_all[ind] == p2_all[ind]:
                    ind += 1
                else:
                    equality = False
    else :
        a=0

print(victory_p1)