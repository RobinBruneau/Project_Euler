

n=5

def mult_same_digit(digit,k):
    for l in range(2,7):
        number = l*k
        digit_n = list(str(number))
        digit_n.sort()
        if digit != digit_n :
            return False
    return True


for k in range(n):
    for j in range(10*10**k,17*10**k):
        digit = list(str(j))
        digit.sort()
        if mult_same_digit(digit,j):
            print(j)

