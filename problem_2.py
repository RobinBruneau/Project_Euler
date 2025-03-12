

def fibonachi(n):
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        return fibonachi(n-1) + fibonachi(n-2)


'''
continuer = True
ind = 0
while continuer:
    if fibonachi(ind)>4000000:
        continuer = False
        print(ind-1)
    ind+=1
'''
sum = 0
for k in range(2,33,3):
    sum += fibonachi(k)
print(sum)

