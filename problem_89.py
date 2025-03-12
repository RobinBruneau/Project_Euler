from tools import *
import numpy as np

conv = {"M":0,"D":1,"C":2,"L":3,"X":4,"V":5,"I":6}

def write_number(n):

    mille = n//1000
    cent = (n-mille*1000)//100
    diz =  (n-mille*1000-cent*100)//10
    unit = (n-mille*1000-cent*100-diz*10)//1

    str_number = mille*"M"
    if cent != 0 :
        if cent == 4 :
            str_number += "CD"
        elif cent == 5 :
            str_number += "D"
        elif cent == 9 :
            str_number += "CM"
        elif cent >= 1 and cent < 4 :
            str_number += cent*"C"
        else :
            str_number += "D"+(cent-5)*"C"

    if diz != 0 :
        if diz == 4 :
            str_number += "XL"
        elif diz == 5 :
            str_number += "L"
        elif diz == 9 :
            str_number += "XC"
        elif diz >= 1 and diz < 4 :
            str_number += diz*"X"
        else :
            str_number += "L"+(diz-5)*"X"

    if unit != 0 :
        if unit == 4 :
            str_number += "IV"
        elif unit == 5 :
            str_number += "V"
        elif unit == 9 :
            str_number += "IX"
        elif unit >= 1 and unit < 4 :
            str_number += unit*"I"
        else :
            str_number += "V"+(unit-5)*"I"

    return str_number


f=open("problem_89.txt","r")
normal = 0
opti = 0
for line in f :
    line = line.split("\n")[0]
    normal += len(line)
    l = [0,0,0,0,0,0,0]
    valid = True
    ind = 0
    for e in line :
        l[conv[e]] += 1
    nb = l[0]*1000+l[1]*500+l[2]*100+l[3]*50+l[4]*10+l[5]*5+l[6]*1
    if True :
        if "CD" in line :
            nb -= 200
        if "CM" in line :
            nb -= 200
        if "XL" in line :
            nb -= 20
        if "XC" in line :
            nb -= 20
        if "IV" in line :
            nb -= 2
        if "IX" in line :
            nb -= 2
    str_nb = write_number(nb)
    opti += len(str_nb)


f.close()
print(normal-opti)
