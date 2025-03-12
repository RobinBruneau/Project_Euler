import copy
from tqdm import tqdm
import numpy as np

def decrypted(l):
    lp = np.array([64,32,16,8,4,2,1])
    l_ascii = []
    l_decrypted = []
    for k in range(len(l)//7):
        val = l[k*7:(k+1)*7]
        ascii = np.sum(val*lp)
        letter = chr(ascii)
        l_ascii.append(ascii)
        l_decrypted.append(letter)
    return l_ascii,l_decrypted

f=open("problem_59.txt","r")
data = f.readline()
data = data.split("\n")[0]
numbers = data.split(",")

l_bin_crypted = ""
for num in numbers:
    bin_num = bin(int(num))[2:]
    if len(bin_num) != 7 :
        bin_num = (7-len(bin_num))*"0"+bin_num
    l_bin_crypted += bin_num

l_bin_crypted = np.array(list(l_bin_crypted)).astype(bool)

for i in tqdm(range(97,123)):
    for j in range(97,123):
        for k in range(97,123):
            number_key = [i,j,k]

            l_key = ""
            for num in number_key:
                aa = bin(num)
                bin_num = bin(num)[2:]
                if len(bin_num) != 7:
                    bin_num = (7 - len(bin_num)) * "0" + bin_num
                l_key += bin_num
            l_key_full = copy.copy(l_key)
            while len(l_key_full)<len(l_bin_crypted):
                l_key_full = l_key_full + l_key
            l_key_full = l_key_full[:len(l_bin_crypted)]
            a=0

            l_key_full = np.array(list(l_key_full)).astype(bool)


            c = np.logical_xor(l_key_full, l_bin_crypted)
            l1,l2 = decrypted(c)
            ln="".join(l2)
            words = ["introduction"]
            for w in words :
                if w in ln :
                    print(i,j,k)
                    print(ln)
                    print(np.sum(l1))